## Install

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


**Ollama Setup**
```
curl https://ollama.ai/install.sh | sh
ollama pull llama2
OLLAMA_HOST=0.0.0.0:11435 ollama serve
```