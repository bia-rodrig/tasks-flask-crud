from flask import Flask


app = Flask(__name__)

# Rota -> Comunicar com outros clientes
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/about')
def about():
    return 'Página sobre'

if __name__ == "__main__":
	app.run(debug=True) # somente se executarmos o sofware de maneira manual, é que vai rodar o debug
