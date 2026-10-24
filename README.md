# California Housing Assignment 3

**Eman Fatima – FA24-BSE-131** · Machine Learning Fundamentals (AIC354)

**Live app:** https://californiahousingml.streamlit.app/

Dataset: https://www.kaggle.com/datasets/camnugent/california-housing-prices (all 20,640 districts)

Five regression algorithms (Ridge, Lasso, Elastic Net, Bayesian Ridge, Extra Trees) are compared with 10-fold cross-validation using RMSE.

| Rank | Algorithm | Mean RMSE (USD) |
|---|---|---|
| 1 | Extra Trees | 52,295 |
| 2 | Bayesian Ridge | 68,907 |
| 3 | Ridge | 68,916 |
| 4 | Lasso | 68,943 |
| 5 | Elastic Net | 69,564 |

## Files

| File | Purpose |
|---|---|
| `california_housing_10fold.ipynb` | Notebook (data, 10-fold CV, timing, model training, prediction) |
| `housing.csv` | Original Kaggle dataset |
| `housing_model.joblib` | Trained Extra Trees pipeline (scikit-learn 1.6.1, compressed) |
| `comparison_results.csv`, `fold_results.csv`, `timings_CPU.csv` | Cross-validation results and execution times |
| `streamlit_app.py`, `requirements.txt` | Streamlit web app |

## Run on Google Colab

1. Upload the notebook to Google Colab and **Run all**; upload `housing.csv` when prompted.
2. Run once on a **CPU** runtime and once on a **T4 GPU** runtime to record execution times (`timings_CPU.csv`, `timings_GPU.csv`).

## Deploy on Streamlit Community Cloud

1. Keep `streamlit_app.py`, `requirements.txt` and `housing_model.joblib` in a public GitHub repository.
2. On https://share.streamlit.io: **Create app**, main file `streamlit_app.py`, Python 3.12.
3. Paste the app URL at the top of the notebook and of this README.

Predictions describe 1990 district medians and are for educational use only.
