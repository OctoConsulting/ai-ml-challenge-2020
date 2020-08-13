import text_preprocessing
import pandas as pd

def word_count(df):
    total_counts = dict()
    counts_unaccepted = dict()
    counts_accepted = dict()
    for index, row in df.iterrows():
        clause_id, sentence, classification = row[0], row[1], row[2]
        lower = text_preprocessing.apply_text_preprocessing(str(sentence), lc=True, rm_spchar=True, rm_num=True, rm_nwln=True, rm_punct=True,
                             rm_whtspc=True, rm_stpwrds=True, stem=False, lemm=False)
        words = lower.split()

        if classification == 0:
            for word in words:
                if word in counts_accepted:
                    counts_accepted[word] += 1
                else:
                    counts_accepted[word] = 1
        if classification == 1:
            for word in words:
                if word in counts_unaccepted:
                    counts_unaccepted[word] += 1
                else:
                    counts_unaccepted[word] = 1

        for word in words:
            if word in total_counts:
                total_counts[word] += 1
            else:
                total_counts[word] = 1

    return total_counts, counts_accepted, counts_unaccepted

def jaccard_similarity(acc, unacc):
    total_acc = sum(acc.values())
    total_unacc = sum(unacc.values())
    similarity = 0
    for key, value in acc.items():
        if key in unacc:
            similarity += (min(acc[key]/total_acc, unacc[key]/total_unacc))
    print(similarity)



if __name__ == '__main__':
    csv_file = "data/AI_ML_Challenge_Training_Data_Set_1_v1_clean.csv"
    df_np = pd.read_csv(csv_file)
    total_counts, accepted, unaccepted = word_count(df_np)
    jss = jaccard_similarity(accepted, unaccepted)
    # sort_total = sorted(total_counts.items(), key=lambda x: x[1], reverse=True)
    # sort_acc = sorted(accepted.items(), key=lambda x: x[1], reverse=True)
    # sort_unacc = sorted(unaccepted.items(), key=lambda x: x[1], reverse=True)

    # print(sort_total)
    # print(sort_acc)
    # print(sort_unacc)
    # print(sum(unaccepted.values()))