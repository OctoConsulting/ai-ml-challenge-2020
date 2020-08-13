# accepts a CSV file, separates each clause into individual sentences and keeps the associated 0 or 1 acceptability
# processes each sentence (removes numbers, punctuation, does stemming, removes stop words, does lemmatiziation)
# writes the sentences into a new CSV and saves it in the working directory


from clause_parsing import parse_sentences
from text_preprocessing import apply_text_preprocessing
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def clean_up_CSV(csv_file):
    df_np = np.asarray(pd.read_csv(csv_file))

    # Separate each clause into individual sentences
    new_csv = []
    for row in df_np:
        clause_id, clause_text, classification = row[0], row[1], row[2]
        clause_sentences = parse_sentences(clause_text)
        for sentence in clause_sentences:
            clean_sentence = apply_text_preprocessing(sentence, lc=False, rm_stpwrds=False, stem=False, lemm=False)
            if clean_sentence:
                new_csv.append([clause_id, clean_sentence, classification])
    df = pd.DataFrame(new_csv, columns=['clause_id', 'sentence', 'classification'])
    df.to_csv("data/AI_ML_Challenge_Training_Data_Set_1_v1_clean.csv", index=False)

    # Split according to label
    df_accepted = df[df['classification'] == 0]
    df_rejected = df[df['classification'] == 1]

    # Train-test split
    df_acc_full_train, df_acc_test = train_test_split(df_accepted, train_size=train_test_ratio, random_state=1)
    df_rej_full_train, df_rej_test = train_test_split(df_rejected, train_size=train_test_ratio, random_state=1)

    # Train-valid split
    df_acc_train, df_acc_valid = train_test_split(df_acc_full_train, train_size=train_valid_ratio, random_state=1)
    df_rej_train, df_rej_valid = train_test_split(df_rej_full_train, train_size=train_valid_ratio, random_state=1)

    # Concatenate splits of different labels
    df_train = pd.concat([df_acc_train, df_rej_train], ignore_index=True, sort=False)
    df_valid = pd.concat([df_acc_valid, df_rej_valid], ignore_index=True, sort=False)
    df_test = pd.concat([df_acc_test, df_rej_test], ignore_index=True, sort=False)

    # Write preprocessed data
    df_train.to_csv('data/train.csv', index=False)
    df_valid.to_csv('data/valid.csv', index=False)
    df_test.to_csv('data/test.csv', index=False)


if __name__ == '__main__':
    train_test_ratio = 0.10
    train_valid_ratio = 0.80
    csv_path = "../../../data/AI_ML_Challenge_Training_Data_Set_1_v1.csv"
    clean_up_CSV(csv_path)