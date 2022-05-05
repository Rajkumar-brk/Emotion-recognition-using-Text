#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
import re
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from tensorflow import keras 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, GRU, Dense


# In[9]:

def main(text):
    num_classes = 5
    embed_num_dims = 300
    max_seq_len = 500
    class_names = ['joy', 'fear', 'anger', 'sadness', 'neutral']
    
    
    # In[10]:
    
    
    data_train = pd.read_csv('data/data_train.csv', encoding='utf-8')
    data_test = pd.read_csv('data/data_test.csv', encoding='utf-8')
    
    X_train = data_train.Text
    X_test = data_test.Text
    
    y_train = data_train.Emotion
    y_test = data_test.Emotion
    
    data = data_train.append(data_test, ignore_index=True)
    
    
    # In[11]:
    
    
    print(data.Emotion.value_counts())
    data.head(6)
    
    
    # In[12]:
    
    
    def clean_text(data):
        
        data = re.sub(r"(#[\d\w\.]+)", '', data)
        data = re.sub(r"(@[\d\w\.]+)", '', data)
        
        data = word_tokenize(data)
        
        return data
    
    
    # In[13]:
    
    
    texts = [' '.join(clean_text(text)) for text in data.Text]
    texts_train = [' '.join(clean_text(text)) for text in X_train]
    texts_test = [' '.join(clean_text(text)) for text in X_test]
    
    
    # In[14]:
    
    
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(texts)
    sequence_train = tokenizer.texts_to_sequences(texts_train)
    sequence_test = tokenizer.texts_to_sequences(texts_test)
    index_of_words = tokenizer.word_index
    vocab_size = len(index_of_words) + 1
    print('Number of unique words: {}'.format(len(index_of_words)))
    
    
    # In[15]:    
    
    X_train_pad = pad_sequences(sequence_train, maxlen = max_seq_len )
    X_test_pad = pad_sequences(sequence_test, maxlen = max_seq_len )
    
    X_train_pad
    
    
    # **Categorize** labels: 
    
    # In[16]:
    
    
    encoding = {
        'joy': 0,
        'fear': 1,
        'anger': 2,
        'sadness': 3,
        'neutral': 4
    }
    
    # Integer labels
    y_train = [encoding[x] for x in data_train.Emotion]
    y_test = [encoding[x] for x in data_test.Emotion]
    
    
    # In[17]:
    
    
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    
    y_train
    
    
    # In[18]:
    
    
    def create_embedding_matrix(filepath, word_index, embedding_dim):
        vocab_size = len(word_index) + 1  # Adding again 1 because of reserved 0 index
        embedding_matrix = np.zeros((vocab_size, embedding_dim))
        with open(filepath,encoding="utf8") as f:
            for line in f:
                word, *vector = line.split()
                if word in word_index:
                    idx = word_index[word] 
                    embedding_matrix[idx] = np.array(
                        vector, dtype=np.float32)[:embedding_dim]
        return embedding_matrix
    
    
    
    
    from tensorflow.keras.models import load_model
    #predictor = load_model('biLSTM_w2v.h5')
    predictor = load_model('biLSTM_w2v.h5',compile=False)
    num_classes = 5
    embed_num_dims = 300
    max_seq_len = 500
    class_names = ['joy', 'fear', 'anger', 'sadness', 'neutral']
    
    import time
    
    #message = text
    
    message = [text]
    
    seq = tokenizer.texts_to_sequences(message)
    padded = pad_sequences(seq, maxlen=max_seq_len)
    
    start_time = time.time()
    pred = predictor.predict(padded)
    
    print('Message: ' + str(message))
    print('predicted: {} ({:.2f} seconds)'.format(class_names[np.argmax(pred)], (time.time() - start_time)))
    res=class_names[np.argmax(pred)]
    return res

# In[ ]:

#main("delivery was hour late and my pizza was cold!")


