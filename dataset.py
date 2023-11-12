from datasets import load_dataset

dataset = load_dataset("urvog/llama2_transcripts_healthcare_callcenter", split="train")

print(dataset[0])

for idx, t in enumerate(dataset):

    with open(f"./text_data/{idx}-text.txt", "w") as f:
        f.write(t["text"])