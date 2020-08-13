from transformers import BertTokenizer
from collections import defaultdict


# TODO: check the max length of the training sentences and set as the tokenizer max length

pretrained_model = 'bert-base-uncased'
# pretrained_model = 'bert-base-cased'
tokenizer = BertTokenizer.from_pretrained(pretrained_model, do_lower_case=True)

test_sentence = 'Test tokenization sentence. Followed by another sentence'

tokens = tokenizer.tokenize(test_sentence)
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(tokens)
print(token_ids)

encoding = tokenizer.encode_plus(
    test_sentence,
    max_length=32,
    truncation=True,
    add_special_tokens=True, # Add '[CLS]' and '[SEP]'
    return_token_type_ids=False,
    pad_to_max_length=True,
    return_attention_mask=True,
    return_tensors='pt',  # Return PyTorch tensors
)
encoding.keys()
# dict_keys(['input_ids', 'attention_mask'])

print(len(encoding['input_ids'][0]))
print(encoding['input_ids'][0])
print(len(encoding['attention_mask'][0]))
print(encoding['attention_mask'])

# # precalculation of pad length, so that we can reuse it later on
# padding_length = max_length_test - len(input_ids)
# # map tokens to WordPiece dictionary and add pad token for those text shorter than our max length
# input_ids = input_ids + ([0] * padding_length)
# # attention should focus just on sequence with non padded tokens
# attention_mask = [1] * len(input_ids)
# # do not focus attention on padded tokens
# attention_mask = attention_mask + ([0] * padding_length)
# # token types, needed for example for question answering, for our purpose we will just set 0 as we have just one sequence
# token_type_ids = [0] * max_length_test
# bert_input = {"token_ids": input_ids,
#     "token_type_ids": token_type_ids,
#     "attention_mask": attention_mask}
#
# print(bert_input)