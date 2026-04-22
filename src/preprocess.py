import pandas as pd

def apply_preprocessing(df, encoders, features):
    # Kategorik sütunları encode et
    for col, le in encoders.items():
        if col in df.columns:
            df[col] = le.transform(df[col])
    
    # Eksik feature'ları 0 ile doldur, sırayı garantiye al
    for col in features:
        if col not in df.columns:
            df[col] = 0
    return df[features]