import subprocess
import os
import sys

# Ruta a tu entorno virtual y app
venv_path = os.path.abspath(".venv\\Scripts\\activate.bat")
app_path = os.path.abspath("app.py")

# Comando que activa el entorno y corre Streamlit
command = f'cmd /k "{venv_path} && streamlit run {app_path}"'
subprocess.call(command, shell=True)
