import model_evaluation
import clause_parsing
import pandas as pd

def main_pipeline(doc_path):
    sentences = clause_parsing.extract_all_clauses(doc_path)
    confidence_score, classification = model_evaluation.classify_sentences(sentences)
    dict = {'clause': sentences, 'confidence_score': confidence_score, 'classification': classification}
    df = pd.DataFrame(dict)
    return df.to_json(orient="table")


if __name__ == '__main__':
    test_doc = "../../../reference/sample_eula_1.pdf"
    output = main_pipeline(test_doc)
    print(output)