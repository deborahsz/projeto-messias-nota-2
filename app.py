from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('courses'))
    return render_template('login.html')

@app.route('/courses')
def courses():
    courses = [
        {"name": "Programação Orientada a Objetos", "description": "Aprenda os conceitos de POO e aplique em Python."},
        {"name": "Estruturas de Dados", "description": "Estude estruturas como listas, pilhas e filas."},
        {"name": "Banco de Dados", "description": "Entenda os princípios de bancos de dados relacionais."},
        {"name": "Redes de Computadores", "description": "Explore os fundamentos das redes de computadores."},
        {"name": "Segurança da Informação", "description": "Saiba como proteger dados e sistemas contra ameaças."},
        {"name": "Inteligência Artificial", "description": "Descubra os princípios e aplicações da IA."},
    ]
    return render_template('courses.html', courses=courses)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)