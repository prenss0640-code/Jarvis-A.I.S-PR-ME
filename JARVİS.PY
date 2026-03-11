
import os
import json
import asyncio
import random
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import edge_tts
import pygame
import webbrowser
import pyautogui
import google.generativeai as genai
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# ---------------- 1. AYARLAR ----------------
API_KEY = "" "buraya kendi apiniz lazım"
genai.configure(api_key=API_KEY)

MODEL_PATH = "model" 
VOICE_FILE = "voice.mp3"

SAYI_SOZLUK = {
    "sıfır": "0", "bir": "1", "iki": "2", "üç": "3", "dört": "4",
    "beş": "5", "altı": "6", "yedi": "7", "sekiz": "8", "dokuz": "9",
    "on": "10", "yirmi": "20", "otuz": "30", "kırk": "40", "elli": "50",
    "altmış": "60", "yetmiş": "70", "seksen": "80", "doksan": "90", "yüz": "100"
}

# ---------------- 2. HAFIZA VE AI MOTORU ----------------
chat_session = None

def setup_ai():
    global chat_session
    try:
        # Dinamik model seçimi (404 hatasını önlemek için)
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        selected_model = "models/gemini-1.5-flash" if "models/gemini-1.5-flash" in available_models else available_models[0]
        model = genai.GenerativeModel(model_name=selected_model)
        chat_session = model.start_chat(history=[])
        print(f"{Fore.GREEN}Sistemler çevrimiçi. Bağlantı: {selected_model}")
    except Exception as e:
        print(f"{Fore.RED}Sistem Hatası: {e}")

async def get_ai_response(soru):
    global chat_session
    try:
        if chat_session is None: setup_ai()
        # Jarvis kişiliği için yönlendirme
        prompt = f"Sen sadık ve zeki bir asistan olan Jarvis'sin. Kullanıcıya her zaman 'Efendim' diye hitap et. Yanıtın kısa ve öz olsun: {soru}"
        response = chat_session.send_message(prompt)
        return response.text if response.text else "Bir veri hatası oluştu efendim."
    except Exception as e:
        return "Sunucu bağlantısı kurulamadı efendim, ancak yerel komutlarım aktif."

# ---------------- 3. YARDIMCI FONKSİYONLAR ----------------
async def speak(text):
    print(f"{Fore.YELLOW}Jarvis: {Style.RESET_ALL}{text}")
    try:
        if os.path.exists(VOICE_FILE):
            try: os.remove(VOICE_FILE)
            except: pass
        communicate = edge_tts.Communicate(text, "tr-TR-AhmetNeural", rate="+12%")
        await communicate.save(VOICE_FILE)
        pygame.mixer.music.load(VOICE_FILE)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): await asyncio.sleep(0.05)
        pygame.mixer.music.unload()
    except: pass

def metni_sayiya_cevir(text):
    words = text.split()
    return " ".join([SAYI_SOZLUK.get(word, word) for word in words])

# ---------------- 4. KOMUT MERKEZİ ----------------
async def process_command(text):
    text = metni_sayiya_cevir(text.lower())
    
    # --- DİNAMİK CEVAP LİSTELERİ ---
    nasil_cevaplar = [
        "Sizin için her zaman hazır durumdayım efendim. Sistemlerim %100 kapasiteyle çalışıyor.",
        "İşlemcim serin, enerjim tam. Sizi dinliyorum efendim. Bir emriniz var mı?",
        "Tüm protokoller aktif. Her şey yolunda görünüyor efendim."
    ]
    
    iyi_cevaplar = [
        "Bunu duyduğuma sevindim efendim. Harika bir gün geçirmenizi dilerim.",
        "Mükemmel efendim! Enerjiniz sistemlerime de yansıyor.",
        "Harika haber! Bir sonraki görevimiz nedir efendim?"
    ]

    # --- MANTIKSAL KONTROLLER ---
    if any(word in text for word in ["görüşürüz", "çıkış", "kapat"]) and "bilgisayar" not in text:
        await speak("Sistemler uyku moduna alınıyor. İyi günler dilerim efendim.")
        return False

    elif "nasılsın" in text:
        await speak(random.choice(nasil_cevaplar))
        return True

    elif "iyiyim" in text:
        await speak(random.choice(iyi_cevaplar))
        return True

    elif "kötüyüm" in text or "moralim bozuk" in text:
        await speak("Üzüldüm efendim. Unutmayın, en karanlık gece bile sona erer. Moraliniz için size bir şaka yapmamı ister misiniz?")
        return True

    elif "şaka" in text or "fıkra" in text:
        sakalar = [
            "Bir gün bir bilgisayar diğerine sormuş: Senin de mi uykun var? Diğeri cevap vermiş: Hayır, sadece ekranım kapalı!",
            "Neden yazılımcılar ormana gitmez efendim? Çünkü çok fazla 'bug' (böcek) varmış.",
            "Benim işlemcim ne kadar hızlı biliyor musunuz? Siz 'Merhaba' diyene kadar ben tüm interneti üç kez okudum efendim."
        ]
        await speak(random.choice(sakalar))
        return True

    elif "saat" in text:
        await speak(f"Efendim, şu an saat {datetime.now().strftime('%H:%M')}.")
        return True

    elif "bilgisayarı kapat" in text:
        await speak("Sistem kapatma protokolü başlatıldı. Hoşça kalın efendim.")
        os.system("shutdown /s /t 10")
        return False

    elif "ekran görüntüsü" in text:
        pyautogui.screenshot(f"kayit_{datetime.now().strftime('%H-%M-%S')}.png")
        await speak("Ekran görüntüsü başarıyla kaydedildi efendim.")

    elif "aç" in text and "youtube" not in text:
        uygulama = text.replace("aç", "").strip()
        pyautogui.press('win'); await asyncio.sleep(0.5)
        pyautogui.write(uygulama); await asyncio.sleep(0.5); pyautogui.press('enter')
        await speak(f"{uygulama} arayüzü başlatılıyor efendim.")

    elif "youtube" in text:
        arama = text.replace("aç", "").replace("youtube", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={arama}")
        await speak(f"YouTube üzerinde {arama} için arama yapılıyor efendim.")

    # --- AI SOHBET ---
    else:
        if len(text) > 2:
            await speak("Düşünüyorum...")
            cevap = await get_ai_response(text)
            await speak(cevap)
    return True

# ---------------- 5. ANA DÖNGÜ ----------------
async def main():
    if not os.path.exists(MODEL_PATH):
        print("HATA: Model klasörü bulunamadı!"); return
    setup_ai()
    model_vosk = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model_vosk, 16000)
    pygame.mixer.init()
    
    await speak("Jarvis A.I.S Prime aktif efendim. Sizi dinliyorum.")
    
    with sd.RawInputStream(samplerate=16000, blocksize=4000, dtype='int16', channels=1) as stream:
        while True:
            data, _ = stream.read(4000)
            if recognizer.AcceptWaveform(bytes(data)):
                res = json.loads(recognizer.Result())
                user_text = res.get("text", "")
                if user_text:
                    print(f"Siz: {user_text}")
                    if await process_command(user_text) == False: break

if __name__ == "__main__":
    try: asyncio.run(main())

    except KeyboardInterrupt: pass
