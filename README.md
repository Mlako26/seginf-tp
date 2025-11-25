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

No se olviden de abrir el puerto 8080 para que sea accesible desde internet

Para saber que tokens fueron emitidos correr:

```bash
sqlite3 honeytokens.db "SELECT id FROM issued_tokens;"
```

Para saber que tokens fueron accedidos correr:

```bash
sqlite3 honeytokens.db "SELECT id, token FROM access_logs;"
```

### CLI Tool

La herramienta puede correrse con los siguiente comandos:

```bash
cd src/cli
python3 tokensnare-cli.py
```

Notar que para ejecutarse, el servidor web debe de estar levantado.

Los scripts de generación de Tokens pueden encontrarse en la carpeta `src/cli/tokens`, y deben de contener clases que implementen la interfaz encontrada en el archivo `honeytoken.py` que se encuentra enel mismo directorio. Un ejemplo de cómo hacerlo es el token ya implementado para markdowns.

La idea de la interfaz es que todos los tokens reciban como mínimo:

- `output_path`: Dónde dejar el token.
- `endpoint_base_uri`: A qué endpoint llamar del webserver. Es una uri "base" ya que luego puede extenderse con lo que el token en particular necesite. Por ejemplo, si en un markdown se requiere importar algo de tipo `.img`, entonces puede realizarse un GET a `{endpoint_base_uri}.img`.
- `kwargs`: Cualquier otro argumento que requiera ese token en específico.

#### markdown.py

Ejemplo de uso:

```bash
python3 tokensnare-cli.py markdown -i ../../README.md -o secret_info.md
```

ese markdown si es agregado a un repo de github cada ves que sea
accedido en el navegador, va a llamar al backend alertando el token fue accedido

[Docs](https://docs.google.com/document/d/1mhF7j0WlURx2hgsLwweNVgSIfIATHDBzwMJvSRAdf6M/edit?tab=t.0)
