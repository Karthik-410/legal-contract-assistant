import spacy

nlp = spacy.load("en_core_web_sm")

def extract_clauses(text):
    clauses = text.split("\n")
    return [c.strip() for c in clauses if len(c.strip()) > 30]

def extract_entities(text):
    doc = nlp(text)
    results = []

    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "DATE", "MONEY", "GPE"]:
            results.append((ent.text, ent.label_))

    return results

def classify_contract(text):
    t = text.lower()

    if "employment" in t:
        return "Employment Contract"
    elif "service" in t:
        return "Service Agreement"
    elif "lease" in t:
        return "Lease Agreement"
    elif "partnership" in t:
        return "Partnership Deed"
    else:
        return "General Contract"

def simple_summary(text):
    return text[:400] + "..."
