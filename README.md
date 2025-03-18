# Descargador de Música con SpotDL

Este script permite descargar canciones desde Spotify utilizando SpotDL y guardarlas en una carpeta específica del sistema. Encuentra automáticamente el archivo más reciente descargado y muestra su ubicación.

## Requisitos

Antes de ejecutar el programa, asegúrate de tener instalados los siguientes requisitos:

- [Python](https://www.python.org/downloads/) (versión 3.12 o superior recomendada)
- [SpotDL](https://github.com/spotDL/spotify-downloader) instalado con:
  ```sh
  pip install spotdl
  ```
- Dependencias de Python:
  ```sh
  pip install os glob subprocess
  ```

## Instalación y Uso

1. Clona este repositorio o descarga el archivo `descarga_musica.py`.
2. Asegúrate de que SpotDL esté correctamente instalado ejecutando en la terminal:
   ```sh
   spotdl --version
   ```
3. Ejecuta el script con Python:
   ```sh
   python descarga_musica.py
   ```
4. Introduce el enlace de la canción de Spotify cuando se solicite.
5. La canción se descargará en la carpeta `C:/Users/POWER/OneDrive/Música` y se mostrará su ubicación en la terminal.

## Código Explicado

- Solicita al usuario el enlace de la canción.
- Descarga el archivo utilizando SpotDL.
- Busca la canción más reciente descargada en la carpeta especificada.
- Muestra la ubicación del archivo descargado.

## Posibles Errores y Soluciones

- **Permiso denegado:** Asegúrate de tener permisos de escritura en la carpeta de destino.
- **SpotDL no encontrado:** Verifica que esté instalado y accesible en la terminal.
- **Python no encuentra módulos:** Reinstala las dependencias con `pip install spotdl`.

## Contribución
Si quieres mejorar el programa, puedes hacer un fork y enviar un pull request.

## Autor
Desarrollado por Juan Camilo Muñoz

