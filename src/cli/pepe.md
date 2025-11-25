# Seguridad de la Información

## TP1 - TokenSnare

Por ahora, para ejecutar todas las pruebas, hace falta generar un entorno virtual con ambos requirements para la CLI tool y el webserver. Eventualmente el webserver se hosteara en un docker con las dependencias instaladas.

Desde el directorio raiz del repo:

``` bash
python3 -m venv venv
source venv/bin/activate
pip install -r src/requirements.txt
```

### Web Server

Para iniciar el webserver, ejecutar el siguiente comando:

```bash
python3 src/server/backend.py
```

no se olviden de abrir el puerto 8080 para que sea accesible desde internet

para saber que tokens fueron emitidos correr:
    $ sqlite3 honeytokens.db "SELECT id FROM issued_tokens;"

para saber que tokens fueron accedidos correr:
    $ sqlite3 honeytokens.db "SELECT id, token FROM access_logs;"

### CLI Tool

La herramienta puede correrse con los siguiente comandos:

```bash
cd src/cli
python3 tokensnare-cli.py
```

Los scripts de generación de Tokens pueden encontrarse en la carpeta `src/cli/tokens`, y deben de contener clases que implementen la interfaz encontrada en el archivo `honeytoken.py` que se encuentra enel mismo directorio.

Por ahora el 

#### markdown.py

Ejemplo de uso:

```bash
python3 tokensnare-cli.py -o my_new_token.md markdown -i ../../README.md
```

ese markdown si es agregado a un repo de github cada ves que sea
accedido en el navegador, va a llamar al backend alertando el token fue accedido

[Docs](https://docs.google.com/document/d/1mhF7j0WlURx2hgsLwweNVgSIfIATHDBzwMJvSRAdf6M/edit?tab=t.0)


![status](http://190.19.111.22:8080/resource/yGbfhm_8Y_4.png)
