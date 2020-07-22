# source: https://www.geeksforgeeks.org/text-preprocessing-in-python-set-1/
# all functions have a string as input and a string as output
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer


def text_lowercase(text):
    # convert to lowercase
    return text.lower()


def remove_numbers(text):
    # remove numbers
    return re.sub(r'\d+', '', text)


def remove_newline(text):
    # remove newline
    return re.sub(r'\n+', '', text)


def remove_punctuation(text):
    # remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def remove_whitespace(text):
    # remove whitespace from text
    return " ".join(text.split())


def remove_stopwords(text):
    # remove stopwords
    # note that this preprocessing step may negatively affect results because it removes words like not
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)


def stem_words(text):
    # stem words in the list of tokenized words using the Porter Stemming algorithm
    stemmer = PorterStemmer()
    word_tokens = word_tokenize(text)
    stems = [stemmer.stem(word) for word in word_tokens]
    return ' '.join(stems)


def lemmatize_word(text):
    # lemmatize string
    # note you may need to define custom lemmatization for words like indemnify, indemnity, indemnification
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(text)
    # provide context i.e. part-of-speech
    lemmas = [lemmatizer.lemmatize(word, pos ='v') for word in word_tokens]
    return ' '.join(lemmas)