# TODO List

## Parte 1 - Investigación

- [x] Investigar formatos de archivos que permiten incrustar `Call Homes`.
  - [Investigación](https://docs.google.com/document/d/1mhF7j0WlURx2hgsLwweNVgSIfIATHDBzwMJvSRAdf6M/edit?tab=t.0)

## Parte 2 - Desarrollo de la Herramienta "TokenSnare"

- [ ] tokensnare-cli
  - App de CLI que permite generar los honeytokens
  - Ej: `python tokensnare-cli.py --type pdf --output carnada.pdf --message "Informe Confidencial Q3"`
  - Yo crearía un script python x cada tipo de archivo y después desde la CLI se llama a cada script.
  - [ ] HoneyTokens
    - [ ] Terminar de cerrar qué honey tokens vamos a hacer (mínimo 5)
    - [ ] Ivo: Hacer script QR
    - [ ] Lore: Hacer script Binario
    - [ ] Manu: Hacer scrip Mysql Dump
    - [ ] Gonza: Hacer script que copia pagina web
    - [X] Gonza: Hacer script markdown
    - [ ] Lore: Hacer script Mail
    - [ ] Hacer script Excel
    - [ ] Hacer script Docs
    - [ ] Hacer script PDF
  - [x] Manu: CLI
    - [x] Hacer que levante una config con la address
    - [x] Ver al final si queremos refactorizarla un poco
- [X] Gonza-Ivo: tokensnare-server
  - [X] Elegir cómo hacer el servidor web (Flask, FastAPI, express.js, etc)
  - [X] Hacer endpoint para registrar nuevos tokens
  - [X] Hacer endpoint para recibir los GETS de los tokens
  - [ ] Hacer enpoint (`/metrics`, `/{token-id}`?) que tenga el registro de los accesos
  - [X] Hacer una mini db con accesos y el registro de los tokens
  - [X] Dockerizar
- [ ] Lore: Informe
  - [ ] Importar alguna plantilla
  - [ ] Portada
  - [ ] Introducción teórica
    - Explicar honeytokens e investigación de los diferentes formatos
  - [ ] Diseño e Implementación
    - [ ] Describir arquitectura de CLI
    - [ ] Describir arquitectura de webserver
    - [ ] Decisiones de diseño??
    - [ ] Explicar cómo se generan cáda uno de los tokens
  - [ ] Manual de Uso y Prueba
    - [ ] Instrucciones de ejecución y environment (hay que armar un docker compose)
    - [ ] Comandos exactos
    - [ ] Screenshots (generando tokens, activandolos, alerta en el server)
