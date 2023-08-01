import spacy

class NERProcessor:
    def __init__(self):
        # Cargando el modelo spaCy NER para Español
        self.nlp_es = spacy.load("es_core_news_sm")

    # Procesando el texto recibido y retornando las entidades nombradas
    def process_text(self, sentences):
        results = []

        for sentence in sentences:
            doc = self.nlp_es(sentence)
            entities = {}
            for ent in doc.ents:
                entities[ent.text] = ent.label_
            results.append({"oración": sentence, "entidades": entities})
    
        return results