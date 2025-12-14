from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "Aprender é um processo, não um destino.",
    "Código limpo é um código gentil com o futuro.",
    "Todo grande projeto começou pequeno.",
]

@app.get("/random")
def random_quote():
    return jsonify({"quote": random.choice(QUOTES)})

if __name__ == "__main__":
    app.run(debug=True)
