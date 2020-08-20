import pandas as pd
import numpy as np
from clause_parsing import parse_sentences
from text_preprocessing import apply_text_preprocessing
import model_evaluation

def val_file_processing(csv_file):
    df_np = np.asarray(pd.read_csv(csv_file))

    # Separate each clause into individual sentences
    new_csv = []
    for row in df_np:
        clause_id, clause_text = row[0], row[1]
        clause_sentences = parse_sentences(clause_text)
        for sentence in clause_sentences:
            clean_sentence = apply_text_preprocessing(sentence, lc=False, rm_stpwrds=False, stem=False, lemm=False)
            if clean_sentence:
                new_csv.append([clause_id, clean_sentence])
    df = pd.DataFrame(new_csv, columns=['clause_id', 'sentence'])
    df.to_csv('validiation_file_clean.csv', index=True)



def get_classifications(val_file):
    df = pd.read_csv(val_file)
    new_csv = []
    for index, row in df.iterrows():
        clause_id, sentence = row['clause_id'], row['sentence']
        prob,classification = model_evaluation.classify_sentence(sentence)
        new_csv.append([clause_id, prob, classification])
        new_df = pd.DataFrame(new_csv, columns=['clause_id', 'prob', 'classification'])
        new_df.to_csv('validation_predictions_2.csv', index=True)

def get_classifications_F1(val_file):
    df = pd.read_csv(val_file)
    new_csv = []
    for index, row in df.iterrows():
        clause_id, sentence, classification = row['clause_id'], row['sentence'], row['classification']
        prob,pred_class = model_evaluation.classify_sentence(sentence)
        new_csv.append([clause_id, sentence, classification, prob, pred_class])
        new_df = pd.DataFrame(new_csv, columns=['clause_id', 'sentence', 'classification', 'prob', 'pred_class'])
        new_df.to_csv('validation_f1.csv', index=True)


def final_cleanup(val_file):
    df = pd.read_csv(val_file)
    clause_ids = df.clause_id.unique()
    new_csv = []
    for id in clause_ids:
        clause_rows = df.loc[df['clause_id'] == id]
        prob_acc = clause_rows.prob.min()*100
        classification = int(clause_rows.loc[clause_rows.prob.idxmin()].classification)
        new_csv.append([id, classification, prob_acc])
    df = pd.DataFrame(new_csv, columns = ['Clause ID', 'Prediction', 'Probability Acceptable'])
    df.to_csv('OctoConsulting Validation Data File.csv',index=False)



if __name__ == '__main__':
    # VAL_FILE_PATH = "../../../data/AI_ML_Challenge_Validation_Data_Set_v1.csv"
    # val_file_processing(VAL_FILE_PATH)
    # CLEAN_VAL_FILE_PATH = "validiation_file_clean.csv"
    # CLEAN_VAL_FILE_PATH = "validation_file_clean_2.csv"
    # get_classifications(CLEAN_VAL_FILE_PATH)
    # VAL_FILE_PATH = "validation_predictions.csv"
    # final_cleanup(VAL_FILE_PATH)

    VAL_FILE_PATH = "validation.csv"
    get_classifications_F1(VAL_FILE_PATH)
