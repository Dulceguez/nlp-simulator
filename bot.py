import json
import re

# Cargar respuestas desacopladas
with open("respuestas.json", encoding="utf-8") as f:
    RESPUESTAS = json.load(f)

def detectar_intencion(texto_usuario):
    """
    Simula un motor de NLP por reglas / keywords.
    Transforma texto libre en una intencion de negocio clasificada.
    """
    texto = texto_usuario.lower()

    # Limpieza basica de puntuacion
    texto_limpio = re.sub(r'[^\w\s]', '', texto)

    # Reglas de clasificacion de intencion (Intent Recognition)
    if any(k in texto_limpio for k in ["saldo", "cuanta plata", "cuanto tengo", "dinero"]):
        return "saldo"
    elif any(k in texto_limpio for k in ["transferir", "transferencia", "enviar plata"]):
        return "transferencia"
    elif any(k in texto_limpio for k in ["rojo", "perdii", "perdi", "robo", "robaron"]):
        return "bloqueo"
    else:
        return "desconocido"

def iniciar_simulador():
    print("===========================================")
    print("Asistente Virtual ICBC (Simulador de NLP/Flows)")
    print("Escribi 'salir' para terminar la prueba.")
    print("===========================================")
    print("Asistencia: Hola! Soy tu asistente virtual. En que te puedo ayudar hoy?\n")

    while True:
        entrada = input("Usuario: ").strip()
        if entrada.lower() in ["salir", "exit", "quit"]:
            print("Asistente: Gracias por usar el asistente! Que tengas buen dia")
            break

        if not entrada:
            continue

        # 1.Detectar intencion (Data-driven/NLP layer)
        intencion = detectar_intencion(entrada)

        #2. Registrar/loguear metrica simulada (mentalidad Design Ops / Data-driven)
        print(f"    [LOGS - NLP Debug] Intencion detectada: '{intencion}'")

        #3. Devolver espuesta centrada en el usuario (Customer Centricity)
        respuesta = RESPUESTAS.get(intencion, RESPUESTAS["desconocido"])
        print(f"Asistente: {respuesta}\n")

if __name__ == "__main__":
    iniciar_simulador()