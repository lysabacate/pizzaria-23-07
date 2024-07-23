from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/cardapio')
def cardapio():

    pizzas = [{'sabor': 'Camarão', 'preco': '150', 'imagem': 'camarao.jpg'},
              {'sabor': 'Calabreza', 'preco': '50', 'imagem': 'calabresa.webp'},
              {'sabor': 'Nordestina', 'preco': '60', 'imagem': 'nordestina.jpg'},
              {'sabor': 'Frango com Catupiry', 'preco': '55', 'imagem': 'pizza.webp'},
              {'sabor': 'Quatro queijos', 'preco': '70', 'imagem': 'pizza.webp'},
              {'sabor': 'Marguerita', 'preco': '60', 'imagem': 'pizza.webp'},
              {'sabor': 'Havaiana', 'preco': '65', 'imagem': 'pizza.webp'},
              {'sabor': 'Três quejos', 'preco': '45', 'imagem': 'pizza.webp'}, 
              {'sabor': 'Portugesa', 'preco': '60', 'imagem': 'pizza.webp'},
              {'sabor': 'Doce de leite', 'preco': '50', 'imagem': 'pizza.webp'},
              {'sabor': 'Chocolate', 'preco': '50', 'imagem': 'pizza.webp'},
            ]

    return render_template('cardapio.html', pizzas=pizzas)