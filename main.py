from flask import Flask, request, jsonify
from processing  import NERProcessor

app = Flask(__name__)
ner_processor = NERProcessor() # Creando instancia de clase para procesar spaCy

@app.route('/ner_es', methods=['POST'])
def ner_es():
    data = request.get_json()
    sentences = data.get('oraciones')

    if sentences is None:
        return jsonify({'error': 'Lista de oraciones no encontrada'}), 400

    entities = ner_processor.process_text(sentences)
    return jsonify({'resultado': entities})

if __name__ == '__main__':
    app.run()