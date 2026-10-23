# Biblioteca Universitaria UDL-ICO

Aplicación web multipágina desarrollada con Flask y Bootstrap para presentar la
información general de una biblioteca universitaria, su catálogo, sus servicios y
sus medios de contacto. Los datos de contacto son ficticios y se usan únicamente
para esta práctica.

## Elementos implementados

- `server.py`: punto de entrada de Flask. Define las rutas de Inicio (`/`),
  Catálogo (`/catalogo`), Servicios (`/servicios`) y Contacto (`/contacto`).
  Cada ruta utiliza `render_template()` y envía las variables `titulo` y
  `mensaje` a su plantilla.
- `templates/layout.html`: plantilla base con la estructura HTML, la referencia
  a Bootstrap 4 y el menú horizontal común. Los enlaces se generan con
  `url_for()`.
- `templates/index.html`: bienvenida, propósito de la biblioteca y horario.
- `templates/catalogo.html`: descripción de libros, revistas, tesis y recursos
  digitales.
- `templates/servicios.html`: descripción de los servicios principales.
- `templates/contacto.html`: dirección, correo electrónico ficticio y horario.
- `requirements.txt`: dependencia Flask necesaria para ejecutar la aplicación.

Las cuatro páginas heredan de `layout.html` con `{% extends "layout.html" %}` y
colocan su contenido en `{% block content %}`. El contenido se organiza mediante
`container-fluid`.

## Requisitos

- Python 3.9 o posterior.
- pip.

## Instalación y ejecución

Desde la carpeta del proyecto, crea y activa el entorno virtual e instala las
dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r .\requirements.txt
python server.py
```

Si PowerShell bloquea la activación de scripts, ejecuta la aplicación con el
intérprete del entorno virtual:

```powershell
.\.venv\Scripts\python.exe -m pip install -r .\requirements.txt
.\.venv\Scripts\python.exe .\server.py
```

Abre <http://127.0.0.1:5050/> en el navegador. Puedes navegar a las demás
páginas usando el menú o visitando `/catalogo`, `/servicios` y `/contacto`.

## URL de GitHub

[https://github.com/axel-lopez524/biblioteca-](https://github.com/axel-lopez524/biblioteca-)
