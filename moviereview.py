#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[2]:

def main(mssg):
        
    # This is how the Naive Bayes classifier expects the input
    def create_word_features(words):
        useful_words = [word for word in words if word not in stopwords.words("english")]
        my_dict = dict([(word, True) for word in useful_words])
        return my_dict
    
    
    # In[4]:
    
    
    #import nltk
    #nltk.download('stopwords')
    
    
    # In[5]:
    
    
    create_word_features(["the", "quick", "brown", "quick", "a", "fox"])
    
    
    # In[8]:
    
    
    with open("neg_reviews.json", 'r') as f:
        score = json.load(f)
        
    neg_reviews = score
    # for fileid in movie_reviews.fileids('neg'):
    #     words = movie_reviews.words(fileid)
    #     neg_reviews.append((create_word_features(words), "negative"))
    # print(neg_reviews)
    # print(len(neg_reviews))
    
    
    # In[7]:
    
    
    #import nltk
    #nltk.download('movie_reviews')
    
    
    # In[9]:
    with open("pos_reviews.json", 'r') as f:
        score = json.load(f)
    
    pos_reviews = score
    # for fileid in movie_reviews.fileids('pos'):
    #     words = movie_reviews.words(fileid)
    #     pos_reviews.append((create_word_features(words), "positive"))
    
    print(pos_reviews[0])
    print(len(pos_reviews))
    
    
    # In[10]:
    
    
    train_set = neg_reviews[:750] + pos_reviews[:750]
    test_set =  neg_reviews[750:] + pos_reviews[750:]
    print(len(train_set),  len(test_set))
    
    
    # In[11]:
    
    
    classifier = NaiveBayesClassifier.train(train_set)
    
    
    # In[12]:
    
    
    accuracy = nltk.classify.util.accuracy(classifier, test_set)
    print(accuracy * 100)
    
    
    # In[13]:
    
    
    review_santa = '''
    
    It would be impossible to sum up all the stuff that sucks about this film, so I'll break it down into what I remember most strongly: a man in an ingeniously fake-looking polar bear costume (funnier than the "bear" from Hercules in New York); an extra with the most unnatural laugh you're ever likely to hear; an ex-dope addict martian with tics; kid actors who make sure every syllable of their lines are slowly and caaarreee-fulll-yyy prrooo-noun-ceeed; a newspaper headline stating that Santa's been "kidnaped", and a giant robot. Yes, you read that right. A giant robot.
    
    The worst acting job in here must be when Mother Claus and her elves have been "frozen" by the "Martians'" weapons. Could they be *more* trembling? I know this was the sixties and everyone was doped up, but still.
    '''
    print(review_santa )
    
    
    # In[15]:
    
    
    #import nltk
    #nltk.download('punkt')
    
    
    # In[16]:
    
    
    # words = word_tokenize(review_santa)
    # words = create_word_features(words)
    # val = classifier.classify(words)
    # print(val)
    
    # In[41]:
    
    
    review_spirit = '''
    There are many Marvel Legends. But none are quite as striking and engaging as Morbius. Jared Leto brings this fierce character to life and shows he has more layers than any character from Copshop.
    '''
    print(review_spirit)
    
    
    # In[42]:
    
    
    words = word_tokenize(mssg)
    words = create_word_features(words)
    val=classifier.classify(words)
    print(val)
    return val
# In[ ]:


mssg='''
   There are many Marvel Legends. But none are quite as striking and engaging as Morbius. Jared Leto brings this fierce character to life and shows he has more layers than any character from Copshop.
    '''
#val=main(mssg)
#print("result is", val)
