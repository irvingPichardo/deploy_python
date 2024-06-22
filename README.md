# deploy_python

# Aplicación Flask con Ngrok

## Tabla de Contenidos

1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Configuración e Instalación](#configuración-e-instalación)
3. [Ejecutar la Aplicación](#ejecutar-la-aplicación)
4. [Usar Ngrok](#usar-ngrok)
5. [Endpoints](#endpoints)
6. [Archivos Estáticos](#archivos-estáticos)

## Estructura del Proyecto



- `app.py`: Archivo principal que contiene la aplicación Flask.
- `requirements.txt`: Archivo que contiene las dependencias de Python.
- `.gitignore`: Especifica los archivos y directorios a ignorar por Git.
- `templates/`: Directorio para las plantillas HTML.
  - `index.html`: Plantilla HTML principal.
- `static/`: Directorio para los archivos estáticos (CSS, JavaScript).
  - `style.css`: Estilos CSS personalizados.
  - `script.js`: Funciones JavaScript personalizadas.

## Configuración e Instalación
$ ngrok http 5000

### 1. Clonar el Repositorio

```bash
$ git clone https://github.com/irvingPichardo/deploy_python.git
$ cd deploy_python
