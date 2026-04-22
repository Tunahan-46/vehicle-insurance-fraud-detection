import streamlit as st
from src.predict import make_prediction

st.set_page_config(page_title="Fraud Guard", page_icon="🛡️", layout="centered")

st.title("🛡️ Fraud Guard")
st.markdown("Hasar dosyası bilgilerini girerek anında risk analizi yapın.")
st.divider()

with st.form("fraud_form"):
    st.subheader("Araç & Poliçe Bilgileri")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Müşteri Yaşı", min_value=18, max_value=80, value=35)
        make = st.selectbox("Araç Markası", ["Honda", "Toyota", "Ford", "Mazda", "Chevrolet", "Pontiac", "Accura", "Dodge", "Mercury", "Jaguar", "Nisson", "VW", "Saab", "Saturn", "Porche", "BMW", "Mecedes", "Ferrari", "Lexus"])
        vehicle_category = st.selectbox("Araç Tipi", ["Sport", "Utility", "Sedan"])
        vehicle_price = st.selectbox("Araç Fiyatı", ["less than 20000", "20000 to 29000", "30000 to 39000", "40000 to 59000", "60000 to 69000", "more than 69000"])
        base_policy = st.selectbox("Poliçe Tipi", ["Liability", "Collision", "All Perils"])
        fault = st.selectbox("Kusur", ["Policy Holder", "Third Party"])
        age_of_vehicle = st.selectbox("Araç Yaşı", ["new", "2 years", "3 years", "4 years", "5 years", "6 years", "7 years", "more than 7"])

    with col2:
        accident_area = st.selectbox("Kaza Bölgesi", ["Urban", "Rural"])
        past_claims = st.selectbox("Geçmiş Hasar Sayısı", ["none", "1", "2 to 4", "more than 4"])
        police_report = st.selectbox("Polis Raporu", ["Yes", "No"])
        witness = st.selectbox("Tanık Var mı?", ["Yes", "No"])
        agent_type = st.selectbox("Acente Tipi", ["External", "Internal"])
        driver_rating = st.slider("Sürücü Puanı", 1, 4, 2)
        address_change = st.selectbox("Adres Değişikliği", ["no change", "1 year", "2 to 3 years", "4 to 8 years", "under 6 months"])
        number_of_cars = st.selectbox("Araç Sayısı", ["1 vehicle", "2 vehicles", "3 to 4", "5 to 8", "more than 8"])

    submitted = st.form_submit_button("🔎 Analiz Et", use_container_width=True)

if submitted:
    # Modelin beklediği İNGİLİZCE VE BÜYÜK/KÜÇÜK HARF DUYARLI orijinal isimler:
    input_dict = {
        'Age': age,
        'Make': make,
        'VehicleCategory': vehicle_category,
        'VehiclePrice': vehicle_price,
        'BasePolicy': base_policy,
        'Fault': fault,
        'AgeOfVehicle': age_of_vehicle,
        'AccidentArea': accident_area,
        'PastNumberOfClaims': past_claims,
        'PoliceReportFiled': police_report,
        'WitnessPresent': witness,
        'AgentType': agent_type,
        'DriverRating': driver_rating,
        'AddressChange_Claim': address_change,
        'NumberOfCars': number_of_cars,
        # PolicyType veri setinde genelde Araç Tipi ve Poliçe Tipinin birleşimidir:
        'PolicyType': f"{vehicle_category} - {base_policy}" 
    }

    with st.spinner("Analiz ediliyor..."):
        result, proba = make_prediction(input_dict)

    # Tahmin fonksiyonundan sonra gelen kısım:
    st.divider()
    st.subheader("Sonuç Analizi")

    # Olasılığı yüzdeye çeviriyorum
    risk_skoru = proba * 100

    # Renkli uyarı mantığı (Kırmızı, Sarı, Yeşil)
    if risk_skoru >= 20:
        # %20 ve Üstü: KIRMIZI (st.error)
        st.error(f"❌ YÜKSEK RİSK — Fraud olasılığı: %{risk_skoru:.1f}")
        st.markdown("Bu talep **kritik düzeyde şüpheli** görünüyor. Manuel inceleme yapılması şiddetle önerilir.")
    
    elif 10 <= risk_skoru < 20:
        # %10 ile %20 Arası: SARI (st.warning)
        st.warning(f"⚠️ DİKKAT — Fraud olasılığı: %{risk_skoru:.1f}")
        st.markdown("Bu talep **orta derecede şüpheli** görünüyor. Detaylı kontrol önerilir.")
    
    else:
        # %10 Altı: YEŞİL (st.success)
        st.success(f"✅ DÜŞÜK RİSK — Fraud olasılığı: %{risk_skoru:.1f}")
        st.markdown("Bu talep **normal** görünüyor, güvenle işleme devam edilebilir.")

    # Risk çubuğunu da altına ekleyelim
    st.progress(float(proba), text=f"Sistemsel Risk Seviyesi: %{risk_skoru:.1f}")