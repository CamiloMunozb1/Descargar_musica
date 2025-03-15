from pytube import YouTube
from pydub import AudioSegment
import os


try:
    usuario_link = input("Ingresa el link de la cancion a descargar: ")
    yt = YouTube(usuario_link)
    ruta_audio = yt.streams.filter(only_audio=True).first().download()
    audio = AudioSegment.from_file(ruta_audio,format="mp4")
    ruta_mp3 = os.path.splitext(ruta_audio)[0]+"mp3"
    audio.export(ruta_mp3, format = "mp3")
except Exception as error:
    print(f"Error en el programa: {error}")