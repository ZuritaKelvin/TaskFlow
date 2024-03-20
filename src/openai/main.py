
from openai import OpenAI
key = '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'
# Crea una instancia del cliente de OpenAI
client = OpenAI(api_key=key)

# Realiza una solicitud a la API de ChatGPT
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Utiliza la versión más reciente del modelo
    messages=[
        {"role": "user", "content": "Compon una poesía que explique el concepto de recursión en programación."},
    ]
)

# Imprime la respuesta generada por el modelo
print(completion.choices[0].message)
