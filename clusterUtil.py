import pickle

reviews = pickle.load(open("data/gameReviewDict.p", "rb"))
from clusterGames import *

def clusterTestGame(fText):
    gameName = "Test Game Title.txt"

    return getGameCluster(reviews, gameName, fText)
   
