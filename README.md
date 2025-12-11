# Seguridad de la Información

## TP1 - TokenSnare

### Web Server

Para iniciar el webserver, hay que tener docker instalado y corriendo en el sistema.

Todos los comandos deben de ser ejecutados dentro del directorio del servidor:

```bash
cd src/server
```

Construir:

```bash
docker-compose build
```

Levantar el server:

```bash
docker-compose up -d
```

Bajar el server:

```bash
docker compose down
```

Ver logs:

```bash
docker-compose logs -f
```

Para saber que tokens fueron emitidos correr:

```bash
sqlite3 data/honeytokens.db "SELECT id FROM issued_tokens;"
```

Para saber que tokens fueron accedidos correr:

```bash
sqlite3 data/honeytokens.db "SELECT id, token FROM access_logs;"
```

### CLI Tool

Para ejecutar la herramienta, hace falta generar un entorno virtual con las dependencias.

Desde el directorio raiz del repo:

``` bash
python3 -m venv venv
source venv/bin/activate
pip install -r src/cli/requirements.txt
```

La herramienta puede correrse con los siguiente comandos:

```bash
cd src/cli
python3 tokensnare-cli.py
```

Notar que para ejecutarse, el contenedor con el servidor web debe de estar levantado.

La herramienta utiliza el archivo `src/cli/config.toml` para saber la uri (o ip) y puerto del tokensnare-server con el que comunicarse. Por defecto es `localhost:8080`, conectándose al contenedor local, pero puede eventualmente ser la dirección de un servidor remoto y uno de sus puertos abiertos.

Los generadores de Tokens pueden encontrarse en la carpeta `src/cli/generators/`, y deben de contener una clase que implemente la interfaz `HoneyTokenGenerator` encontrada en el archivo `honeytoken.py`. Un ejemplo de implementación es el generador para markdowns.

La idea de la interfaz es que todos los tokens reciban como mínimo:

- `output_path`: Dónde dejar el token.
- `endpoint_base_uri`: A qué endpoint llamar del webserver. Es una uri "base" ya que luego puede extenderse con lo que el token en particular necesite. Por ejemplo, si en un markdown se requiere importar algo de tipo `.img`, entonces puede realizarse un GET a `{endpoint_base_uri}.img`.
- `kwargs`: Cualquier otro argumento que requiera ese token en específico.

#### webpage.py

Ejemplo de uso:

```bash 
python3 tokensnare-cli.py web-page --url "https://www.google.com" --output "./tokens/google.html"
```

#### markdown.py

Ejemplo de uso:

```bash
python3 tokensnare-cli.py markdown -i ../../README.md -o secret_info.md
```

Ese markdown si es agregado a un repo de github cada ves que sea accedido en el navegador, va a llamar al backend alertando el token fue accedido.

#### mysql_dump.py

Ejemplo de uso:

```bash
python3 ./tokensnare-cli.py mysql-dump -o token.sql
```

El subcomando mysql-dump genera un dump que al ser restaurado alerta al web server. Puede ser generado en base a uno genérico o un dump customizado puede ser provisto con la opción `-i/--input`. Algunas limitaciones actuales de la implementación son:

- No se puede distinguir entre distintos tokens de dumps. Con lo cual, de haber más de uno, la alerta solo podrá reconocer que alguno de ellos se intentó restaurar.
- Las instrucciones de replicación de base de datos, las cuales efectivamente realizan el llamado al servidor web, se están actualmente appendeando al final del dump. Esto puede llegar a ser fácil para un atacante reconocer. En el futuro se debería de correctamente parsear el dump e insertarlas entre medio de instrucciones en una posición aleatoria.
- El dump genérico es estático y chico. En el futuro de ganar popularidad la herramienta, el mismo será fácil de reconocer. Eventualmente se debería de proveer un dump aleatorio.

Para testearlo, proveímos en el compose del web server un contenedor mysql que simluará del gestor de base de datos de un atacante. Al restorear el dump en el contenedor se debería de alertar el servidor web:

```bash
docker exec mysql_client mysql -h honeytokens -P 3306 -u root < <path-to-tokenized-dump> 
```
