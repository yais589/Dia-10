import requests
import time

URL = "http://localhost:11434/api/generate"

prompts = [
    "Explica qué es un LLM",
    "¿Qué es Azure?",
    "¿Qué es Python?",
    "Resume la IA Generativa",
    "Dame 5 ideas de negocio"
]

print("\nBENCHMARK OLLAMA\n")

for prompt in prompts:

    inicio = time.time()

    response = requests.post(
        URL,
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        }
    )

    fin = time.time()

    tiempo = round(fin - inicio, 2)

    print("-" * 50)
    print("Prompt:", prompt)
    print("Tiempo:", tiempo, "segundos")
    print("Longitud respuesta:", len(response.json()["response"]))