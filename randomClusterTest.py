import pickle
import sys
reviews = pickle.load(open("data/gameReviewDict.p", "rb"))
from clusterGames import *

def main():
    f = open(sys.argv[1], 'r')
    fText = '\n'.join(f.readlines())
    f.close()
    
    gameName = sys.argv[1]
    print(getGameCluster(reviews, gameName, fText))
   
main()
