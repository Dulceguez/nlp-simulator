# Simulador de Intenciones para Asistente Conversacional

Prototipo en Python que simula un **motor de reconocimiento de intenciones (*Intent Recognition*)** por reglas y normalización de texto. 

Diseñado desde una perspectiva de **Sistemas + UX / Customer Centricity**: desacopla la lógica de negocio de los copys, implementa trazas de depuración (*debug logs*) orientadas a métricas/observabilidad, y prioriza un *fallback* amigable para el usuario ante ambigüedades.

## Stack

- **Python 3.x** (Logica, CLI loop, manejo de flujos)
- **JSON** (Dataset desacoplado de respuestas/copys)
- **Re / Regex** (Normalización y limpieza básica de input de usuario)

## Como correrlo

1. Parate en la carpeta del proyecto (`cd nlp-simulator` o la carpeta donde tengas los archivos).
2. Ejecutá en tu terminal:
   ```bash
   python bot.py
