import torch
from transformers import BertForSequenceClassification
from transformers import BertTokenizer
import numpy as np
import boto3


def classify_sentences(sent_list):
    print("Encoding sentences for classification")
    # file_save_loc = 'model/downloaded_model.pt'
    # s3 = boto3.client('s3')
    # s3.download_file('BUCKET_NAME', 'OBJECT_NAME', file_save_loc)
    PATH = "model/model.pt"
    # PATH = file_save_loc
    device = torch.device('cpu')
    model = BertForSequenceClassification.from_pretrained(
        "bert-base-uncased", # Use the 12-layer BERT model, with an uncased vocab.
        num_labels = 2, # The number of output labels--2 for binary classification.
                        # You can increase this for multi-class tasks.
        output_attentions = False, # Whether the model returns attentions weights.
        output_hidden_states = False, # Whether the model returns all hidden-states.
    )
    model.load_state_dict(torch.load(PATH, map_location=device))
    model.eval()

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)

    # Tokenize all of the sentences and map the tokens to thier word IDs.
    input_ids = []
    attention_masks = []

    for sent in sent_list:
        # `encode_plus` will:
        #   (1) Tokenize the sentence.
        #   (2) Prepend the `[CLS]` token to the start.
        #   (3) Append the `[SEP]` token to the end.
        #   (4) Map tokens to their IDs.
        #   (5) Pad or truncate the sentence to `max_length`
        #   (6) Create attention masks for [PAD] tokens.
        encoded_dict = tokenizer.encode_plus(
            str(sent),  # Sentence to encode.
            add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
            max_length=128,  # Pad & truncate all sentences.
            truncation=True,
            pad_to_max_length=True,
            return_attention_mask=True,  # Construct attn. masks.
        return_tensors='pt',  # Return pytorch tensors.
        )

        # Add the encoded sentence to the list.
        input_ids.append(encoded_dict['input_ids'])

        # And its attention mask (simply differentiates padding from non-padding).
        attention_masks.append(encoded_dict['attention_mask'])

    print("All sentences encoded")

    # Convert the lists into tensors.
    input_ids = torch.cat(input_ids, dim=0).to(device)
    attention_masks = torch.cat(attention_masks, dim=0).to(device)



    with torch.no_grad():
        print("Performing classifications")
        output = model(input_ids,
                       token_type_ids=None,
                       attention_mask=attention_masks)
        print("Performing softmax")
        sm = torch.nn.Softmax(dim=1)
        probabilities = sm(output[0])
        prob_array = probabilities.numpy()
        prob_accepted = prob_array[:,0]
        pred_class = np.argmax(prob_array, axis=1)
        return (prob_accepted, pred_class)


def classify_sentence(sent):
    PATH = "model/model.pt"
    device = torch.device('cpu')
    model = BertForSequenceClassification.from_pretrained(
        "bert-base-uncased", # Use the 12-layer BERT model, with an uncased vocab.
        num_labels = 2, # The number of output labels--2 for binary classification.
                        # You can increase this for multi-class tasks.
        output_attentions = False, # Whether the model returns attentions weights.
        output_hidden_states = False, # Whether the model returns all hidden-states.
    )
    model.load_state_dict(torch.load(PATH, map_location=device))
    model.eval()

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)

    encoded_dict = tokenizer.encode_plus(
        str(sent),  # Sentence to encode.
        add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        max_length=128,  # Pad & truncate all sentences.
        truncation=True,
        pad_to_max_length=True,
        return_attention_mask=True,  # Construct attn. masks.
        return_tensors='pt',  # Return pytorch tensors.
    )

    with torch.no_grad():
        output = model(**encoded_dict)
        sm = torch.nn.Softmax(dim=0)
        probabilities = sm(output[0][0])
        prob_array = probabilities.numpy()
        prob_accepted = prob_array[0]
        pred_class = np.argmax(prob_array)
        return(prob_accepted, pred_class)


if __name__ == '__main__':
    test_sent = "Except to the extent prohibited under applicable law, you agree to defend, indemnify and hold harmless COMPANY and the COMPANY Parties, and their respective successors and assigns, from and against all claims, liabilities, damages, judgments, awards, losses, costs, expenses and fees"
    classify_sentence(test_sent)