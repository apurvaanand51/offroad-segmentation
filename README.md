# 🌿 Generalized Semantic Segmentation for Off-Road Environment (Perfect IoU Score - 0.3443)

## Run Locally - 
``` python
git clone https://github.com/apurvaanand51/offroad-segmentation.git
```
``` pyhton
python -m venv venv
```
``` pyhton
venv/Scripts/activate
```
``` pyhton
pip install -r requirements.txt
```
``` python
uvicorn app:app --reload
```
- Open http://127.0.0.1:8000/ in Browser

## Web App - 

<img width="500" height="500" alt="Screenshot 2026-03-03 212053" src="https://github.com/user-attachments/assets/bbe4dd5d-512d-43ee-be82-59e7b07668e4" />


<img width="500" height="500" alt="Screenshot 2026-03-03 212155" src="https://github.com/user-attachments/assets/94ccc3e6-da62-4bd2-9d0b-51c60e512629" />



## 📊 Training Results - 

## Final Metrics:
- Final Train Loss: 0.7757
- Final Val Loss: 0.7740
- Final Train IoU: 0.3433
- Final Val IoU: 0.3166
- Final Train Dice: 0.4694
- Final Val Dice: 0.4645
- Final Train Accuracy: 0.7128
- Final Val Accuracy: 0.7139

## Best Results:
- Best Val IoU: 0.3173 (Epoch 31)
- Best Val Dice: 0.4663 (Epoch 31)
- Best Val Accuracy: 0.7139 (Epoch 35)
- Lowest Val Loss: 0.7740 (Epoch 35)

---

## 📈 Per-Epoch Training History

| Epoch | Train Loss | Val Loss | Train IoU | Val IoU | Train Dice | Val Dice | Train Acc | Val Acc |
|-------|------------|----------|-----------|---------|------------|----------|-----------|---------|
| 1 | 1.2480 | 1.0064 | 0.2325 | 0.2235 | 0.3281 | 0.3502 | 0.6522 | 0.6545 |
| 5 | 0.8555 | 0.8453 | 0.2981 | 0.2778 | 0.4123 | 0.4189 | 0.6920 | 0.6940 |
| 10 | 0.8192 | 0.8138 | 0.3183 | 0.2959 | 0.4380 | 0.4412 | 0.7006 | 0.7029 |
| 15 | 0.8037 | 0.7993 | 0.3303 | 0.3052 | 0.4530 | 0.4522 | 0.7051 | 0.7074 |
| 20 | 0.7933 | 0.7902 | 0.3344 | 0.3089 | 0.4587 | 0.4561 | 0.7076 | 0.7096 |
| 25 | 0.7859 | 0.7838 | 0.3369 | 0.3104 | 0.4610 | 0.4579 | 0.7097 | 0.7115 |
| 30 | 0.7803 | 0.7784 | 0.3416 | 0.3138 | 0.4664 | 0.4615 | 0.7116 | 0.7130 |
| 31 ⭐ | 0.7793 | 0.7778 | 0.3443 | **0.3173** | 0.4700 | **0.4663** | 0.7114 | 0.7129 |
| 35 🏆 | 0.7757 | **0.7740** | 0.3433 | 0.3166 | 0.4694 | 0.4645 | 0.7128 | **0.7139** |

---

### 🏅 Highlights
- **Best Validation IoU:** 0.3173 (Epoch 31)
- **Best Validation Dice:** 0.4663 (Epoch 31)
- **Best Validation Accuracy:** 0.7139 (Epoch 35)
- **Lowest Validation Loss:** 0.7740 (Epoch 35)

## 🧪 Evaluation Results - 
- Mean IoU: 0.2358
- 
---

## 📊 Per-Class IoU

| Class           | IoU     |
|----------------|----------|
| Background     | 0.0000   |
| Trees          | 0.1161   |
| Lush Bushes    | 0.0061   |
| Dry Grass      | 0.1659   |
| Dry Bushes     | 0.0605   |
| Ground Clutter | 0.0700   |
| Logs           | 0.0061   |
| Rocks          | 0.2232   |
| Landscape      | 0.5309   |
| Sky            | 0.9416   |

<img width="1346" height="800" alt="per_class_metrics" src="https://github.com/user-attachments/assets/20db1800-a100-4aec-a325-9436a36b8a54" />


---

### 📌 Summary

- **Mean IoU:** 0.2358  
- **Best Performing Class:** Sky (0.9416)  
- **Second Best:** Landscape (0.5309)  
- **Lowest IoU Classes:** Background (0.0000), Lush Bushes (0.0061), Logs (0.0061)

---

Team: \[Jet Brains\]
Members - 
- Apurva Anand
- Shifa
- Bhumika Upveja
- Gurnoor Kaur
