# 🌿 Generalized Semantic Segmentation for Off-Road Environment

### Hack For Green Bharat -- Duality AI

This project focuses on **semantic segmentation of off-road
environments** using synthetic training data to improve environmental
understanding in unstructured terrains.

------------------------------------------------------------------------

## 📌 Project Overview

Autonomous systems operating in rural and off-road environments face
challenges due to: - Lack of structured roads - Irregular terrain -
Limited labeled real-world datasets

To address this, we trained a semantic segmentation model using
synthetic datasets and evaluated it on real-world samples.

------------------------------------------------------------------------

## 🛠️ Environment & Dependency Requirements

### System Requirements

-   Python 3.9+
-   CUDA-enabled GPU (Recommended)
-   8GB+ RAM

### Required Libraries

Install dependencies using:

pip install -r requirements.txt

Or manually:

pip install torch torchvision torchaudio pip install opencv-python pip
install numpy pip install matplotlib pip install tqdm pip install
segmentation-models-pytorch

------------------------------------------------------------------------

## 📂 Project Structure

project/ │ ├── dataset/ │ ├── images/ │ ├── masks/ │ ├── models/ │ └──
best_model.pth │ ├── train.py ├── evaluate.py ├── predict.py ├──
utils.py ├── requirements.txt └── README.md

------------------------------------------------------------------------

## 🚀 Step-by-Step Instructions

### 1️⃣ Clone Repository

git clone `<your-repo-link>`{=html} cd project

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Prepare Dataset

Place images inside: dataset/images/

Place masks inside: dataset/masks/

Ensure filenames match (e.g., image1.jpg & image1.png)

### 4️⃣ Train the Model

python train.py

Best model will be saved to: models/best_model.pth

### 5️⃣ Evaluate the Model

python evaluate.py

Outputs: - Pixel Accuracy - IoU (Intersection over Union) - Mean IoU
(mIoU) - Dice Score

### 6️⃣ Run Inference

python predict.py --image path_to_image.jpg

------------------------------------------------------------------------

## 📊 Reproducing Final Results

Use: - Learning Rate: 1e-4 - Optimizer: Adam - Loss: CrossEntropy + Dice
Loss - Epochs: 30--50

Example:

python train.py --epochs 50 --lr 0.0001 python evaluate.py --model
models/best_model.pth

Expected Results (approx): - mIoU: 0.65 -- 0.80 - Pixel Accuracy: 85%+ -
Dice Score: 0.70+

------------------------------------------------------------------------

## 📈 Understanding Output Metrics

Pixel Accuracy → Percentage of correctly classified pixels.

IoU → Overlap between predicted mask and ground truth.

Dice Score → Similarity between prediction and actual mask.

Higher values indicate better segmentation performance.

------------------------------------------------------------------------

## 📌 Notes

-   Synthetic training improves generalization to unseen terrains.
-   Performance depends on dataset quality and augmentation strategy.
-   GPU training significantly reduces training time.

------------------------------------------------------------------------

## 👨‍💻 Hackathon Submission

Developed for: Hack For Green Bharat -- Duality AI

Team: \[Your Team Name\]
