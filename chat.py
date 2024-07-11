import requests
import json

OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "YYOUR_OPENAI_APIKEY"

def get_response_from_openai(message, messages):
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "You are simple chat bot, helping answer user questions."
            },
            *messages,
            {
                "role": "user",
                "content": message
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(OPENAI_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"].strip()
        else:
            return "No response from AI model."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def main():
    messages = []
    while True:
        message = input("You: ")
        if message.lower() in ["exit", "quit"]:
            break
        
        response = get_response_from_openai(message, messages)
        print(f"Metis: {response}")
        
        messages.append({"role": "user", "content": message})
        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
