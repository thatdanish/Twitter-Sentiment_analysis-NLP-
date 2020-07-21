import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize



len_unique_words = 19111   #value noted from model file
len_max = 37    #value noted from model file
lemma = WordNetLemmatizer()

def call_model():
    model = load_model('Models/final_model.h5')
    return model


def create_data(sent):
    print("******Cleaning Data*******")
    clean_tweets = []
        
    sent = sent.lower()
    clean_sent = sent.translate(str.maketrans("",'',string.punctuation))
    words = word_tokenize(clean_sent)
    clean_words = [i for i in words if i not in stopwords.words('english')]
    lemma_words = [lemma.lemmatize(i) for i in clean_words]
            
    clean_tweets.append(lemma_words)
            
    return clean_tweets

def prep_data(data):
    print('*****Preparing Data*******')
    data = create_data(data)
    tokenizer = Tokenizer(num_words=len_unique_words)
    tokenizer.fit_on_texts(list(data))
    data = tokenizer.texts_to_sequences(data)
    data = sequence.pad_sequences(data,maxlen=len_max)
   
    return data

