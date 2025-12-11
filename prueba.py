import os

# Desactivar proxy solo para localhost
os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["no_proxy"] = "127.0.0.1,localhost"

import ollama
# Leer archivos
with open("./docs/servicios.txt", "r", encoding="utf-8") as f:
    servicios = f.read()

with open("./docs/precios.txt", "r", encoding="utf-8") as f:
    precios = f.read()

with open("./docs/politicas.txt", "r", encoding="utf-8") as f:
    politicas = f.read()

# Crear contexto
contexto = [
    {"role": "system", "content": """
Eres un asistente especializado en JP-VALENCIA.
Usa la información que se te entrega para responder de manera profesional.
"""}
]

print("💬 Chat con Ollama — modelo llama3.1")
print("Escribe 'salir' para terminar.\n")


while True:
    try:
        user = input("Tú: ")
    except KeyboardInterrupt:
        print("\nCerrando chat…")
        break

    if user.lower() == "salir":
        break

    contexto.append({"role": "user", "content": f"{user}\n\nInformación:\n{servicios}\n{precios}\n{politicas}"})
    respuesta = ollama.chat(
        model="jpmodel",
        messages=contexto
    )

    bot = respuesta.get("message", {}).get("content", "(Sin respuesta)")

    print("🤖:", bot)

    contexto.append({"role": "assistant", "content": bot})
