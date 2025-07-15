 Proje Özeti
Bu Python projesi:

✅ Sabah & akşam tansiyonlarını ayrıştırır
✅ K‑Means algoritmasıyla iki gruba ayırır (riskli / normal)
✅ Hangi grubun daha yüksek tansiyon ortalamasına sahip olduğunu bulur
✅ Her bireye "Risk" veya "Normal" etiketi ekler
✅ Eğer toplumun yarısından fazlası riskliyse uyarı verir:
🛑 Yüksek Tansiyon / Kalp Riski

📁 Dosya Yapısı
TSYN/
├── app.py           # Analiz kodları
├── tansiyon.xlsx    # Örnek veri dosyası
└── README.md
⚙️ Kurulum & Çalıştırma
Gerekli kütüphaneleri yükle:
pip install pandas numpy scikit-learn
Script'i çalıştır:
python app.py
✅ Çıktı:
Günlük Risk Durumları
         Tarih    risk
0  2025-07-14  Normal
1  2025-07-15     Risk

Genel Değerlendirme: Yüksek Tansiyon / Kalp Riski
📈 K-Means Neyi Yapıyor?
Kümeleme algoritması, sabah ve akşam sistolik verileri üzerinden bireyleri iki gruba ayırır. Ortalama değeri daha yüksek olan grup "Riskli" olarak etiketlenir.
