# Jarvis-A.I.S-PR-ME
Python ve Gemini AI ile geliştirilmiş, sesli komutlarla çalışan gelişmiş asistan projesi. Jarvis A.I.S Prime: Gelecek burada.
# 🦾 Jarvis A.I.S Prime

Jarvis A.I.S Prime, Python diliyle geliştirilmiş, Google Gemini 1.5 Pro/Flash modellerinden güç alan, sesli komutlarla bilgisayar yönetimi ve yapay zeka sohbeti yapabilen gelişmiş bir asistan projesidir.

## 🌟 Öne Çıkan Özellikler
* **Akıllı Sohbet:** Google Gemini entegrasyonu ile "Efendim" hitaplı, zeki ve kısa yanıtlar.
* **Sesli Komut Sistemi:** Vosk motoru ile internete bağlı olmasanız bile sesli komutları algılama.
* **Sistem Kontrolü:** Ekran görüntüsü alma, bilgisayarı kapatma, uygulama başlatma.
* **Hızlı Erişim:** YouTube aramaları ve web tarayıcı entegrasyonu.
* **Gelişmiş Ses:** `edge-tts` ile gerçeğe yakın Türkçe erkek sesi (AhmetNeural).

## 🛠️ Kurulum Gereksinimleri

### 1. Gerekli Kütüphaneler
Projenin çalışması için terminale (CMD) şu komutu yazarak gerekli kütüphaneleri yükleyin:
```bash
pip install google-generativeai vosk sounddevice edge-tts pygame pyautogui colorama
2. Vosk Çevrimdışı Ses Modeli
Asistanın sizi duyabilmesi için Vosk modeline ihtiyacı vardır:

Vosk Model Sayfası'ndan vosk-model-small-tr-0.3 dosyasını indirin.

İndirdiğiniz klasörün adını model olarak değiştirin ve ana proje klasörünün içine koyun.

⚙️ Yapılandırma
JARVİS.py dosyasını açın ve API_KEY kısmına kendi Google AI Studio anahtarınızı ekleyin:

Python
API_KEY = "BURAYA_KENDI_API_ANAHTARINIZI_YAZIN"
🎤 Kullanım Rehberi
Asistanı başlattıktan sonra aşağıdaki komutları kullanabilirsiniz:

Genel: "Nasılsın?", "Saat kaç?", "Bana bir şaka yap."

Uygulama: "Not defteri aç", "Chrome aç" (Win tuşu üzerinden arama yapar).

Medya: "YouTube'da [Şarkı İsmi] aç."

Güvenlik/Sistem: "Ekran görüntüsü al", "Bilgisayarı kapat."

📜 Lisans
Bu proje MIT Lisansı altında korunmaktadır. Eğitim amaçlı geliştirilmiştir.
Geliştirici: Yusuf Kaan
Versiyon: 2.0
