import streamlit as st
from Modelo.command_model import CommandModel
from Vista.voice_view import VoiceView
from Controlador.voice_controller import VoiceController

st.set_page_config(page_title="SmartVoice", layout="centered")

st.markdown("<h2 style='text-align: center;'>🔊 SmartVoice</h2>", unsafe_allow_html=True)
st.write("Controla tu hogar con tu voz (Prototipo)")
if st.button("🎙️ Escuchar comando"):
    controller = VoiceController()
    view = VoiceView()
    model = CommandModel()

    st.info("Escuchando...")
    command = controller.listen()
    if command:
        response = model.get_action(command)
        st.success(f"✅ Comando: {command}")
        st.write(f"🧠 Acción: {response}")
        view.speak(response)
    else:
        st.error("❌ No se entendió el comando.")

