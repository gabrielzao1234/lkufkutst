from flask import Flask, render_template

app = Flask(__name__)

#Criar a primeira pagina do site
@app.route('/')

def homepage():
    return render_template('homepage.html')


@app.route('/grau')
def contatos():
    return render_template('graudemoto.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html',nome_usuario=nome_usuario)

#Colocar o site no ar

if __name__ == "__main__":
    app.run(debug=True)
