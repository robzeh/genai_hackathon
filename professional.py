import streamlit as st
import os

# Assuming the following directory structure:
# /path/to/recordings/folder/ -> contains audio files
# /path/to/outputs/folder/ -> contains text summaries with the same filenames

recordings_folder_path = './sample_audio'
transcript_folder_path = './sample_audio_transcripts'
outputs_folder_path = './responses'


print(os.listdir('./sample_audio'))
# List all the patient record files (assuming the extension for audio files is .mp3)
patient_records = [f for f in os.listdir(recordings_folder_path) if f.endswith('.wav')]

print(patient_records)

# Create a select box for the user to choose a patient record
selected_record = st.selectbox('Select a patient record', patient_records)

# Display the selected patient's name (assuming the filename structure is 'FirstName_LastName.mp3')
patient_name = selected_record[:-4].replace('_', ' ')  # This removes the file extension and replaces underscores with spaces
st.text('Name: ' + patient_name)

# Display the audio player for the selected patient's recording
audio_file_path = os.path.join(recordings_folder_path, selected_record)
audio_file = open(audio_file_path, 'rb')
st.audio(audio_file.read(), format='audio/wav')

# Display the summary for the selected patient's record
# Assuming the text summaries have the same filename but with .txt extension
transcript_file_path = os.path.join(transcript_folder_path, selected_record.replace('.wav', '.wav-transcript.txt'))
if os.path.exists(transcript_file_path):
    with open(transcript_file_path, 'r') as file:
        transcript_text = file.read()
    st.text('Transcript:')
    st.write(transcript_text)
else:
    st.error('Transcript file does not exist for the selected record.')


summary_file_path = os.path.join(outputs_folder_path, selected_record.replace('.wav', '.wav-transcript.txt-response-with-sum.txt'))
if os.path.exists(summary_file_path):
    with open(summary_file_path, 'r') as file:
        summary_text = file.read()
    st.text('Summary:')
    st.write(summary_text)
else:
    st.error('Summary file does not exist for the selected record.')
