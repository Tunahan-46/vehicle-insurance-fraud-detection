import joblib
import pandas as pd
import os
from src.preprocess import apply_preprocessing # Yeni dosyadan çağırıyoruz

def load_model():
    base = os.path.dirname(__file__)
    model_path = os.path.join(base, '../models/best_fraud_model.joblib')
    data_path = os.path.join(base, '../data/processed/cleaned_data.joblib')
    
    model_info = joblib.load(model_path)
    data_info = joblib.load(data_path)
    
    return model_info['model'], model_info['threshold'], model_info['features'], data_info['encoders']

def make_prediction(input_dict):
    model, threshold, features, encoders = load_model()
    df = pd.DataFrame([input_dict])
    
    # Preprocessing işlemini diğer dosyadan çağırıyoruz
    df_processed = apply_preprocessing(df, encoders, features)
    
    proba = model.predict_proba(df_processed)[:, 1][0]
    is_fraud = proba >= threshold
    
    return is_fraud, proba