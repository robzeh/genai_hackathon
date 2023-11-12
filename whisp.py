import whisper 

# load model 
model = whisper.load_model("medium")

# decode
result = model.transcribe("./data/hello.aac")
print(result["text"])