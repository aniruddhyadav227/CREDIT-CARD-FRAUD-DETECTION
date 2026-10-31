@echo off
echo Environment activate kar raha hu...
call venv\Scripts\activate

echo Model check/train kar raha hu...
python train_model.py

echo Website chalu kar raha hu...
streamlit run app.py
pause







"