# accepts a CSV file, separates each clause into individual sentences and keeps the associated 0 or 1 acceptability
# processes each sentence (removes numbers, punctuation, does stemming, removes stop words, does lemmatiziation)
# writes the sentences into a new CSV and saves it in the working directory


from clause_parsing import parse_sentences
from text_preprocessing import apply_text_preprocessing
import numpy as np
import pandas as pd


def clean_up_CSV(csv_file):
    df_np = np.asarray(pd.read_csv(csv_file))

    new_csv = []
    for row in df_np:
        clause_id, clause_text, classification = row[0], row[1], row[2]
        clause_sentences = parse_sentences(clause_text)
        for sentence in clause_sentences:
            clean_sentence = apply_text_preprocessing(sentence, lc=False, rm_stpwrds=False, stem=False, lemm=False)
            if clean_sentence:
                new_csv.append([clause_id, clean_sentence, classification])
    df = pd.DataFrame(new_csv, columns=['clause_id', 'sentence', 'classification'])
    df.to_csv("../../../data/AI_ML_Challenge_Training_Data_Set_1_v1_clean.csv", index=False)


if __name__ == '__main__':
    csv_path = "../../../data/AI_ML_Challenge_Training_Data_Set_1_v1.csv"
    clean_up_CSV(csv_path)