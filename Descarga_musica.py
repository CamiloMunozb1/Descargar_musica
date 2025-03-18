import subprocess  # Para ejecutar comandos en la terminal desde Python
import os  # Para manejar rutas y archivos
import glob  # Para buscar archivos con un patrón específico

try:
    # Solicitamos al usuario el enlace de la canción que quiere descargar
    usuario_link = input("Ingresa el link de la cancion a descargar: ")

    # Definimos la carpeta donde se guardará la canción descargada
    ruta_audio = "C:/Users/POWER/OneDrive/Música"

    # Ejecutamos el comando de spotdl para descargar la canción en la ruta especificada
    # 'check=True' hace que Python lance un error si el comando falla
    subprocess.run(["spotdl", "download", usuario_link, "--output", ruta_audio], check=True)

    # Buscamos todos los archivos .mp3 dentro de la carpeta de descargas
    archivos_mp3 = glob.glob(os.path.join(ruta_audio, "*.mp3"))

    # Seleccionamos el archivo más reciente (el último descargado) basándonos en la fecha de creación
    mp3_reciente = max(archivos_mp3, key=os.path.getctime)

    # Mostramos el nombre del archivo descargado
    print(f"Descarga finalizada: {mp3_reciente}")

except Exception as error:
    # Capturamos cualquier error que ocurra en la ejecución y lo mostramos en pantalla
    print(f"Error en el programa: {error}")
