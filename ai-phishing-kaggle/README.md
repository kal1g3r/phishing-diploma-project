# Phishing Email Detection (Kaggle) — TF-IDF + Logistic Regression

## Overview
This project demonstrates a simple AI/ML pipeline for phishing email detection using a Kaggle dataset.
The model outputs a **phishing probability (model confidence score)** for a given email.

## Dataset
- Source: Kaggle — *Phishing Email Dataset* (Naser Abdullah Alam)
- File used: `phishing_email.csv`
- Columns:
  - `text_combined` — email text
  - `label` — class label (**0 = legit**, **1 = phishing**)

Dataset link:
https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset

## Method
- Text vectorization: **TF-IDF** (`ngram_range=(1,2)`, `max_features=50000`)
- Classifier: **Logistic Regression** (`solver="liblinear"`, `max_iter=2000`)
- Split: **80/20 train/test**, `stratify=y`, `random_state=42`

## Evaluation (Kaggle run)
- ROC-AUC: ~0.999
- Accuracy / Precision / Recall / F1: ~0.99 (on the dataset test split)

## Demo inference
A sample phishing-like email is passed to the trained model and the output is:
- `phishing probability ≈ 0.985`

## Explainability (local)
For the sample email, the notebook computes local feature contributions:
- contribution ≈ `TF-IDF(feature) * coef(feature)`
This shows which words/phrases pushed the prediction toward **phishing** or **legit**.

## How to run
### Option A: Kaggle
1. Open the notebook in Kaggle
2. Add the dataset as input
3. Run all cells

### Option B: Local (optional)
```bash
pip install -r requirements.txt
jupyter notebook
<img width="587" height="1048" alt="image" src="https://github.com/user-attachments/assets/af49cda5-a0c1-4044-bc90-7f419f312488" />
