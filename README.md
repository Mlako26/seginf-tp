# Seguridad de la Información

## TP1 - TokenSnare

# backend.py
    no se olviden de abrir el puerto 8080 para que sea accesible desde internet

    para saber que tokens fueron emitidos correr:
       $ sqlite3 honeytokens.db "SELECT id FROM issued_tokens;"

    para saber que tokens fueron accedidos correr:
       $ sqlite3 honeytokens.db "SELECT id, token FROM access_logs;"

# markdown.py
    Ejemplo de uso:
        $ python3 markdown.py README.md
        -genera-> README_with_status.md

    ese markdown si es agregado a un repo de github cada ves que sea
    accedido en el navegador, va a llamar al backend alertando el token fue accedido

[Docs](https://docs.google.com/document/d/1mhF7j0WlURx2hgsLwweNVgSIfIATHDBzwMJvSRAdf6M/edit?tab=t.0)
