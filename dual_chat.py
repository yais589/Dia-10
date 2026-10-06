import requests

URL = "http://localhost:11434/api/generate"

print("Backend disponible:")
print("1. Local (Ollama)")

input("Selecciona backend (1): ")

while True:

    prompt = input("\nTú: ")

    if prompt.lower() == "salir":
        break

    response = requests.post(
        URL,
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    print("\nGemma:")
    print(response.json()["response"])