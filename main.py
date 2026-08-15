from googletrans import Translator
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
duration = 5  # kayıt saniyeleri
sample_rate = 44100
print("Şimdi konuşun...")
recording = sd.rec(
  int(duration * sample_rate), # kaydedilecek örnek sayısı
  samplerate=sample_rate,      # örnekleme hızı
  channels=1,                  # 1, mono kayıt anlamına gelir.
  dtype="int16")               # kayıtlı örnekler için veri türü
sd.wait()  # kayıt bitene kadar beklemek
wav.write("output.wav", sample_rate, recording)
print("Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...")
recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio, language="tr")
    print("Şunu söylediniz:", text)
except sr.UnknownValueError:             # - Google gürültü veya sessizlik nedeniyle konuşmayı anlayamadığında
    print("Konuşma tanınamadı.")
except sr.RequestError as e:             # - İnternet bağlantısı yoksa veya API kullanılamıyorsa
    print(f"Hizmet hatası: {e}")
translator = Translator()
translated = translator.translate(text, dest='es')  # buradaki 'es' İspanyolca için bir koddur
print("🌍 İspanyolca'ya çeviri:", translated.text)
