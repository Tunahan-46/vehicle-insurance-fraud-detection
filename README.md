# 🛡️ Fraud Guard: Sigorta Hasar Talebi Risk Analiz Sistemi

Bu proje, sigorta sektöründeki araç hasar dosyalarını analiz ederek dolandırıcılık (fraud) ihtimalini tahmin eden uçtan uca bir Makine Öğrenmesi uygulamasıdır.

## 🚀 Proje Hakkında
Sigorta şirketleri için manuel inceleme süreçleri maliyetli ve zaman alıcıdır. **Fraud Guard**, yapay zeka gücünü kullanarak şüpheli dosyaları saniyeler içinde tespit eder ve risk seviyesine göre müfettişleri uyarır.

## 🛠️ Teknik Özellikler
- **Model:** Random Forest & XGBoost algoritmaları kullanıldı.
- **Optimizasyon:** Veri setindeki dengesizlik (imbalance) durumu `class_weight` ve `Threshold Tuning` (%10 ve %20 kritik eşikler) ile aşılmıştır.
- **Arayüz:** Streamlit kütüphanesi ile hızlı ve etkileşimli bir web paneli geliştirildi.
- **Kod Mimarisi:** Temiz kod prensiplerine uygun, modüler (`predict.py` ve `app.py` ayrı) bir yapı kuruldu.

## 📊 Risk Seviyeleri
Sistem, tahmin edilen olasılığa göre üç farklı görsel uyarı verir:
- ✅ **%0 - %10:** Düşük Risk (Güvenli)
- ⚠️ **%10 - %20:** Orta Risk (Dikkatli Kontrol)
- ❌ **%20+:** Yüksek Risk (Kritik Şüphe / Manuel İnceleme)

## 📂 Dosya Yapısı
```text
├── app.py              # Streamlit arayüz kodları
├── src/
│   └── predict.py      # Model yükleme ve tahmin mantığı
├── models/
│   └── model.joblib    # Eğitilmiş AI modeli
├── requirements.txt    # Gerekli kütüphaneler listesi
└── README.md           # Proje dökümantasyonu

Projeyi yerelinizde çalıştırmak için:

Depoyu klonlayın: git clone <repo-url>

Gerekli paketleri yükleyin: pip install -r requirements.txt

Uygulamayı başlatın: streamlit run app.py

Hazırlayan: Tunahan Özdil