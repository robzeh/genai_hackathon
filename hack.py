import streamlit as st
from st_audiorec import st_audiorec


st.title("GenAI Hackathon")

st.write("Hello")

st.button("click")

symptoms = st.text_input("What are your symptoms?")

st.write(symptoms)

wav_audio_data = st_audiorec()

# st.audio(wav_audio_data, format='audio/wav')
print(wav_audio_data)