import nltk
import string
import os
from sklearn.cluster.dbscan_ import DBSCAN
from sklearn.cluster.dbscan_ import dbscan
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from scipy.spatial import distance
import collections
import pickle
from pprint import pprint

reviews = pickle.load(open("data/gameReviewDict.p", "rb"))

token_dict = {}
stemmer = PorterStemmer()

def process_text(text, stem=True):
    """ Tokenize text and stem words removing punctuation """
    text = text.translate(string.punctuation)
    tokens = word_tokenize(text)
 
    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]
 
    return tokens
 
 
def cluster_text(reviews):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    i=0
    labelDict = {}
    for gameSystemKey, systemDict in reviews.items():
        count = 0
        for gameKey, gameReview in systemDict.items():
            count+=1
            if count > 100:#just to reduce sample size
                break
            if "review" in gameReview:
                lowers = gameReview["review"].lower()
                no_punctuation = lowers.translate(string.punctuation)
                token_dict[gameKey] = no_punctuation

                #print(gameReview["Review"])
                #print(gameKey)
    #sort values by keys

    
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    sortedValues = [token_dict[key] for key in sorted(token_dict.keys())]
    sortedLabels = [key for key in sorted(token_dict.keys())]

    tfidf_model = tfidf.fit_transform(sortedValues).todense()
    eps = .75
    min_samples = 2
                # metric is the function reference, not the string key.
    metric = distance.euclidean
    dbscan_model = DBSCAN(eps=eps, min_samples=min_samples).fit(tfidf_model)
#    dbscan_model.fit(tfidf_model)
 
    tfidf_cluster = collections.defaultdict(list)

    #pprint(dbscan_model.labels_)
    for idx, label in enumerate(dbscan_model.labels_):
        tfidf_cluster[label].append(sortedLabels[idx])
 
    return tfidf_cluster
 

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

for k, v in reviews.items():
    for subKey, gameReview in v.items():
        
        if "review" in gameReview:
            lowers = gameReview["review"].lower()
            no_punctuation = lowers.translate(string.punctuation)
            token_dict[k] = no_punctuation

"""for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        shakes = open(file_path, 'r')
        text = shakes.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(None, string.punctuation)
        token_dict[file] = no_punctuation"""
        
#this can take some time
print(cluster_text(reviews))