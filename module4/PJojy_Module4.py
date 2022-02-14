import pandas as pd
import nltk
import sys
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer

#perform tokenization 
def perform_tokenization(summary):
    token_list = [word_tokenize(summ) for summ in summary]
    return token_list

#perform lemmatization
def perform_lemmatization(token_list):
    lemmatize = WordNetLemmatizer()

    lemmatized_words = []

    for t in token_list:
        summ = []
        for w in t:
            rootWord = lemmatize.lemmatize(w,pos='n')
            summ.append(rootWord)
        lemmatized_words.append(summ)
    return lemmatized_words

#perform stemming
def perform_stemming(token_list):
    ps = PorterStemmer()

    stemmed_words = []

    for t in token_list:
        summ = []
        for w in t:
            rootWord = ps.stem(w)
            summ.append(rootWord)
        stemmed_words.append(summ)
    return stemmed_words



def main():
    #load csv to dataframe
    reviews = pd.read_csv('Musical_instruments_reviews.csv')

    summary = reviews['summary']
    
    token_list = perform_tokenization(summary)
    print(f'PERFORMING TOKENIZATION. Printing First 10 results: \n {token_list[:10]}')
    
    lemmatized_words = perform_lemmatization(token_list)
    print(f'PERFORMING LEMMATIZATION. Printing First 10 results: \n {lemmatized_words[:10]}')
    
    stemmed_words = perform_stemming(token_list)
    print(f'PERFORMING STEMMING. Printing First 10 results: \n {stemmed_words[:10]}')
    
main()
    
    
