import streamlit as st
from Modelo.command_model import CommandModel
from Vista.voice_view import VoiceView
from Controlador.voice_controller import VoiceController

# Configuración para diseño tipo móvil
st.set_page_config(page_title="SmartVoice", layout="centered")

# Estilos personalizados
st.markdown("""
    <style>
        .main {
            padding: 20px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 32px;
            font-size: 16px;
            border-radius: 10px;
            width: 100%;
        }
        .custom-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown("<h2 style='text-align: center;'>🔊 SmartVoice</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Controla tu hogar con tu voz</p>", unsafe_allow_html=True)

st.markdown('<div class="custom-box">', unsafe_allow_html=True)

# Botón principal
if st.button("🎙️ ESCUCHAR COMANDO"):
    st.info("🎧 Escuchando...")
    
    controller = VoiceController()
    view = VoiceView()
    model = CommandModel()

    command = controller.listen()
    if command:
        response = model.get_action(command)
        st.success(f"✅ Comando: {command}")
        st.write(f"🧠 Acción: {response}")
        view.speak(response)
    else:
        st.error("❌ No se entendió el comando.")

st.markdown('</div>', unsafe_allow_html=True)
