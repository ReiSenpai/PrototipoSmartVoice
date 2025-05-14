# hook-streamlit.py

from PyInstaller.utils.hooks import collect_all

# Streamlit tiene varias dependencias, así que usamos collect_all para incluir todo.
# Esto asegura que se recojan todos los archivos necesarios de Streamlit.

datas, binaries, hiddenimports = collect_all('streamlit')

# Puedes incluir más bibliotecas si es necesario
# Si tienes dependencias específicas, las puedes añadir a `hiddenimports`
