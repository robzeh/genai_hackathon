import sys
import whisper
from pathlib import Path

def transcribe_audio(file_path):
    # Load the Whisper model
    model = whisper.load_model("medium")

    # Check if the sample_audio_transcripts directory exists, if not, create it
    transcript_directory = Path("./sample_audio_transcripts")
    transcript_directory.mkdir(parents=True, exist_ok=True)

    # Define the path for the transcript file
    transcript_filename = Path(file_path).stem + "-transcript.txt"
    transcript_path = transcript_directory / transcript_filename

    # Transcribe the provided audio file
    result = model.transcribe(file_path)

    # Write the transcript to the text file
    with open(transcript_path, "w") as file:
        file.write(result["text"])

    print(f"Transcription saved to {transcript_path}")

if __name__ == "__main__":
    # Take the filename as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    # Ensure the file is in the sample_audio directory
    file_path = Path("./sample_audio") / filename
    transcribe_audio(file_path)

