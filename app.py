import os
from gtts import gTTS
import streamlit as st
from io import BytesIO

# Title of the app
st.title("Text to Speech Converter")

# Input text from the user
text_input = st.text_area("Enter text to convert to speech:", "")

# Button to trigger the text-to-speech conversion and play audio
if st.button("Convert and Play"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            # Convert text to speech
            tts = gTTS(text=text_input, lang='en')
            # Save to a bytes buffer
            audio_buffer = BytesIO()
            tts.write_to_fp(audio_buffer)

            # Reset buffer position to start
            audio_buffer.seek(0)

            # Play the audio (in-app)
            st.audio(audio_buffer, format="audio/mp3")

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Sidebar information
st.sidebar.info("A simple text to speech converter using gTTS and Streamlit in English.")
