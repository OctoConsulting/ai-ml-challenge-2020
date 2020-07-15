# The purpose of this file is to parse EULA documents into individual clauses

import nltk


def parse_clauses(body):
    # Input: String of sentences
    # Output: List of tokenized sentences
    tokenizer = nltk.data.load('/punkt/english.pickle')
    return tokenizer.tokenize(body)


if __name__ == '__main__':
    test_text = "There isn't time, so brief is life. And but an instant, so to speak, for that."
    clauses = parse_clauses(test_text)
    print(clauses)