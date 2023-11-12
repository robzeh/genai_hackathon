import os
import json
import requests
import random
from prompts import prompt_no_triage

BASE_URL = os.environ.get('OLLAMA_HOST', 'http://localhost:11435')

# Generate a response for a given prompt with a provided model. This is a streaming endpoint, so will be a series of responses.
# The final response object will include statistics and additional data from the request. Use the callback function to override
# the default handler.
def generate(model_name, prompt, system=None, template=None, format="", context=None, options=None, callback=None):
    try:
        url = f"{BASE_URL}/api/generate"
        payload = {
            "model": model_name, 
            "prompt": prompt, 
            "system": system, 
            "template": template, 
            "context": context, 
            "options": options,
            "format": format,
        }
        
        # Remove keys with None values
        payload = {k: v for k, v in payload.items() if v is not None}
        
        with requests.post(url, json=payload, stream=True) as response:
            response.raise_for_status()
            
            # Creating a variable to hold the context history of the final chunk
            final_context = None
            
            # Variable to hold concatenated response strings if no callback is provided
            full_response = ""

            # Iterating over the response line by line and displaying the details
            for line in response.iter_lines():
                if line:
                    # Parsing each line (JSON chunk) and extracting the details
                    chunk = json.loads(line)
                    
                    # If a callback function is provided, call it with the chunk
                    if callback:
                        callback(chunk)
                    else:
                        # If this is not the last chunk, add the "response" field value to full_response and print it
                        if not chunk.get("done"):
                            response_piece = chunk.get("response", "")
                            full_response += response_piece
                            # print(response_piece, end="", flush=True)
                    
                    # Check if it's the last chunk (done is true)
                    if chunk.get("done"):
                        final_context = chunk.get("context")
            
            # Return the full response and the final context
            return full_response, final_context
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None


def generate_summary(transcript, system_prompt):
    print(f"processing file {transcript}")
    # open file
    f = open(f"./sample_audio_transcripts/{transcript}", "r")
    user_prompt = f.read()

    # generate response
    full_resp = generate("llama2", user_prompt, system_prompt)
    print(full_resp)
    with open(f"./responses/{transcript}-response.txt", "w") as f:
        f.write(full_resp[0])


if __name__ == "__main__":

    # generate summaries for 10 random files
    text_files = os.listdir("./sample_audio_transcripts")

    for f in text_files:
        generate_summary(f, prompt_no_triage)
