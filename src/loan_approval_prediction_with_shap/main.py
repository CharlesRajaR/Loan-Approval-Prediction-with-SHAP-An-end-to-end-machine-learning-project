

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "loan_approval_prediction_with_shap"/ "data" / "raw"


print(f" \n Path: {RAW_DATA_DIR}\n")