# 811 Assistant

**The Problem**: 811 is the non-emergency healthcare line which provides everyday health information and advice.
However, 811 experiences high volume of calls with shortage of workers.

**Our solution**: Create a tool that streamlines healthcare workers ability to provide 811 assistance.
Our tool creates a transcript from an audio input.
We then use an LLM to create a summary of the audio, allowing the healthcare worker to easier understand the patients situation.

## Install

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Ollama Setup**
Ollama is used to host LLaMa2 locally. `ollama.py` will call this local api to generate summaries.
```
curl https://ollama.ai/install.sh | sh
ollama pull llama2
OLLAMA_HOST=0.0.0.0:11435 ollama serve
```

## File Structure

```
/genai_hackathon
- /sample_audio/                # sample audio files
- /sample_audio_transcripts/    # sample audio files transcripts
- /text_data/                   # hugging face dataset of healthcare call center
- /dataset.py                   # python code to call ollama api
- /patient.py                   # streamlit app for patient
- /professional.py              # streamlit app for healthcare professional
- /prompts.py                   # system prompts we experimented with
- /ollama.py                    # take a transcript, generate summary for it
```
