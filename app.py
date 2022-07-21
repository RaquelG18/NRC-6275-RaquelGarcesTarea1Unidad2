import uuid
import logging
from flask import Flask, render_template, request
from flask_sessionstore import Session
from flask_session_captcha import FlaskSessionCaptcha
from pymongo import MongoClient

# Inicializamos la aplicación y la carpeta template
app = Flask(__name__, template_folder="template")

# configuracion de la base de datos
mongoClient = MongoClient('localhost', 27017)

# configuración del Captcha
app.config["SECRET_KEY"] = uuid.uuid4()
app.config['CAPTCHA_ENABLE'] = True

# permite 5 caracteres en el captcha
app.config['CAPTCHA_LENGTH'] = 5

# Setea los captcha height and width
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60
app.config['SESSION_MONGODB'] = mongoClient
app.config['SESSION_TYPE'] = 'mongodb'

# Enables server session
Session(app)

# Initialize FlaskSessionCaptcha
captcha = FlaskSessionCaptcha(app)

# creamos el decorador para la ruta principal y agregamos los metodos get y post 
@app.route('/', methods=['POST', 'GET'])
def index():  # Creamos la función
    if request.method == "POST":
        if captcha.validate():
            return "success"
        else:
            return "fail"
# Redirección a la pagina formulario.html
    return render_template("formulario.html")

 # Creamos el main para que la app se pueda ejecutar
if __name__ == "__main__":
    app.debug = True
    logging.getLogger().setLevel("DEBUG")
    app.run()
