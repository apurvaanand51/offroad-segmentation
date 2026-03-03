import torch
import torch.nn.functional as F
from torch import nn
import torchvision.transforms as transforms
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse, HTMLResponse
from PIL import Image
import numpy as np
import cv2
import io

app = FastAPI()

# =============================
# CONFIG
# =============================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

w = int(((960 / 2) // 14) * 14)
h = int(((540 / 2) // 14) * 14)
n_classes = 10

color_palette = np.array([
    [0, 0, 0],
    [34, 139, 34],
    [0, 255, 0],
    [210, 180, 140],
    [139, 90, 43],
    [128, 128, 0],
    [139, 69, 19],
    [128, 128, 128],
    [160, 82, 45],
    [135, 206, 235],
], dtype=np.uint8)

transform = transforms.Compose([
    transforms.Resize((h, w)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# =============================
# MODEL
# =============================

class SegmentationHeadConvNeXt(nn.Module):
    def __init__(self, in_channels, out_channels, tokenW, tokenH):
        super().__init__()
        self.H, self.W = tokenH, tokenW

        self.stem = nn.Sequential(
            nn.Conv2d(in_channels, 128, kernel_size=7, padding=3),
            nn.GELU()
        )

        self.block = nn.Sequential(
            nn.Conv2d(128, 128, kernel_size=7, padding=3, groups=128),
            nn.GELU(),
            nn.Conv2d(128, 128, kernel_size=1),
            nn.GELU(),
        )

        self.classifier = nn.Conv2d(128, out_channels, 1)

    def forward(self, x):
        B, N, C = x.shape
        x = x.reshape(B, self.H, self.W, C).permute(0, 3, 1, 2)
        x = self.stem(x)
        x = self.block(x)
        return self.classifier(x)


print("Loading DINOv2 backbone...")
backbone = torch.hub.load("facebookresearch/dinov2", "dinov2_vits14")
backbone.to(device)
backbone.eval()

# Get embedding dimension
dummy = torch.randn(1, 3, h, w).to(device)
with torch.no_grad():
    emb = backbone.forward_features(dummy)["x_norm_patchtokens"]
n_embedding = emb.shape[2]

print("Loading segmentation head...")
model = SegmentationHeadConvNeXt(
    in_channels=n_embedding,
    out_channels=n_classes,
    tokenW=w // 14,
    tokenH=h // 14
)

model.load_state_dict(torch.load("best_segmentation_head.pth", map_location=device))
model.to(device)
model.eval()

print("Model ready!")

# =============================
# UTILS
# =============================

def mask_to_color(mask):
    h, w = mask.shape
    color_mask = np.zeros((h, w, 3), dtype=np.uint8)
    for class_id in range(n_classes):
        color_mask[mask == class_id] = color_palette[class_id]
    return color_mask


def create_side_by_side(original_pil, pred_mask):
    original = original_pil.resize((w, h))
    original_np = np.array(original)

    pred_color = mask_to_color(pred_mask)

    combined = np.hstack((original_np, pred_color))
    return combined


# =============================
# API ENDPOINT
# =============================

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    img_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        features = backbone.forward_features(img_tensor)["x_norm_patchtokens"]
        logits = model(features)
        outputs = F.interpolate(logits, size=(h, w), mode="bilinear", align_corners=False)
        pred_mask = torch.argmax(outputs, dim=1)[0].cpu().numpy()

    comparison = create_side_by_side(image, pred_mask)

    _, buffer = cv2.imencode(".png", cv2.cvtColor(comparison, cv2.COLOR_RGB2BGR))
    return StreamingResponse(io.BytesIO(buffer.tobytes()), media_type="image/png")


# =============================
# SIMPLE WEB UI
# =============================

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Offroad Segmentation Demo</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 40px;">
        <h2>offroad-semantic-segmentation using Duality</h2>
        <p>Upload an image and see the prediction</p>

        <form id="upload-form">
            <input type="file" id="file-input" accept="image/*" required />
            <br><br>
            <button type="submit" style="padding:10px 20px;">Predict</button>
        </form>

        <br>
        <h3>Result (Original | Prediction)</h3>
        <img id="result-image" width="1000"/>

        <script>
            const form = document.getElementById('upload-form');

            form.addEventListener('submit', async (e) => {
                e.preventDefault();

                const fileInput = document.getElementById('file-input');
                const file = fileInput.files[0];

                const formData = new FormData();
                formData.append("file", file);

                const response = await fetch("/predict", {
                    method: "POST",
                    body: formData
                });

                const blob = await response.blob();
                const imageUrl = URL.createObjectURL(blob);
                document.getElementById("result-image").src = imageUrl;
            });
        </script>
    </body>
    </html>
    """