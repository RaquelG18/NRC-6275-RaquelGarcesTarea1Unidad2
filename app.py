from flask import Flask, render_template

# Inicializamos la aplicación y la carpeta template
app = Flask(__name__, template_folder="template")

#creamos el decorador para la ruta principal 
@app.route("/")
def index():  # Creamos la función
    # Redirección a la pagina formulario.html
    return render_template('formulario.html')


 # Creamos el main para que la app se pueda ejecutar
if __name__ == '__main__':
    app.run(debug=True)