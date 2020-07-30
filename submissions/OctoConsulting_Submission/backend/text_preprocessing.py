# source: https://www.geeksforgeeks.org/text-preprocessing-in-python-set-1/
# all functions have a string as input and a string as output
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer


def _text_lowercase(text):
    # convert to lowercase
    return text.lower()


def _remove_special_characters(text):
    return re.sub('[^A-Za-z0-9 ]+', '', text)


def _remove_numbers(text):
    # remove numbers
    return re.sub(r'\d+', '', text)


def _remove_newline(text):
    # remove newline
    return re.sub(r'\n+', '', text)


def _remove_punctuation(text):
    # remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def _remove_whitespace(text):
    # remove whitespace from text
    return " ".join(text.split())


def _remove_stopwords(text):
    # remove stopwords
    # note that this preprocessing step may negatively affect results because it removes words like not
    english_stopwords = nltk.data.load('/nltk_data/corpora/stopwords/english.txt')
    # stop_words = set(stopwords.words(english_stopwords))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in english_stopwords]
    # filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)


def _stem_words(text):
    # stem words in the list of tokenized words using the Porter Stemming algorithm
    stemmer = PorterStemmer()
    word_tokens = word_tokenize(text)
    stems = [stemmer.stem(word) for word in word_tokens]
    return ' '.join(stems)


def _lemmatize_word(text):
    # lemmatize string
    # note you may need to define custom lemmatization for words like indemnify, indemnity, indemnification
    lemmatizer = WordNetLemmatizer()
    print(lemmatizer)
    word_tokens = word_tokenize(text)
    # provide context i.e. part-of-speech
    lemmas = [lemmatizer.lemmatize(word, pos ='v') for word in word_tokens]
    return ' '.join(lemmas)


def apply_text_preprocessing(sentence, lc=True, rm_spchar=True, rm_num=True, rm_nwln=True, rm_punct=True,
                             rm_whtspc=True, rm_stpwrds=True, stem=True, lemm=True):
    # input: single sentence as a string, any changes from the default settings of preprocessing
    # output: processed sentence
    if lc: sentence = _text_lowercase(sentence)
    if rm_spchar: sentence = _remove_special_characters(sentence)
    if rm_num: sentence = _remove_numbers(sentence)
    if rm_nwln: sentence = _remove_newline(sentence)
    if rm_punct: sentence = _remove_punctuation(sentence)
    if rm_whtspc: sentence = _remove_whitespace(sentence)
    if rm_stpwrds: sentence = _remove_stopwords(sentence)
    if stem: sentence = _stem_words(sentence)
    if lemm: sentence = _lemmatize_word(sentence)
    return sentence