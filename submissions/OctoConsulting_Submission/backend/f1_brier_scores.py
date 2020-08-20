import pandas as pd
from sklearn.metrics import f1_score, brier_score_loss

def get_f1(val_file):
    df = pd.read_csv(val_file)
    y_true = df['classification'].values
    y_pred = df['pred_class'].values
    print("F1 score is " + str(f1_score(y_true, y_pred)))
    print("Weighted F1 score is " + str(f1_score(y_true, y_pred, average='weighted')))


def get_brier(val_file):
    df = pd.read_csv(val_file)
    y_true = df['classification'].values
    y_pred = df['pred_class'].values
    prob = df['prob'].values
    prob[y_pred==1] = 1- prob[y_pred==1]
    print("Brier score is " + str(brier_score_loss(y_true, prob, pos_label=0)))



if __name__ == '__main__':
    VAL_FILE = 'validation_f1.csv'
    get_f1(VAL_FILE)
    get_brier(VAL_FILE)