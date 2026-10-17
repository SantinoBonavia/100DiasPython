from gtts import gTTS
texto=input("Ingrese el texto a convertir en audio: ")
tts=gTTS(text=texto, lang="es")
tts.save("audio.mp3")

print("Audio generado!")