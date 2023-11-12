import streamlit as st
from st_audiorec import st_audiorec


st.title("GenAI Hackathon")

st.write("Please describe your symptoms")
wav_audio_data = st_audiorec()

print(wav_audio_data)