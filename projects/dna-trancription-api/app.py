from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<seq>')
def process(seq):
    dna_seq = seq.upper()
    output = dna_seq.translate(dna_seq.maketrans('ATGC','UACG'))
    return jsonify(result = output)