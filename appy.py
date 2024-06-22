from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/relativity')
def relativity_vs_quantum():
    response = {
        "question": "¿Por qué la relatividad y la física cuántica son incompatibles?",
        "answer": ("La teoría de la relatividad de Einstein y la física cuántica son dos pilares "
                   "fundamentales de la física moderna. Sin embargo, son incompatibles porque "
                   "describen fenómenos en escalas diferentes y usan principios diferentes. "
                   "La relatividad general explica la gravedad y el universo a gran escala, "
                   "mientras que la física cuántica describe las partículas subatómicas y "
                   "sus interacciones. Integrarlas en una teoría coherente ha sido un desafío "
                   "para los físicos, conocido como el problema de la gravedad cuántica.")
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
