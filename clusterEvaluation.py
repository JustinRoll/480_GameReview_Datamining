import clusterGames
import reviewGoldStandard
import pickle
#load all reviews from the gold standard
#   check if there are reviews from the gold standard that didn't get parsed correctly; discard those
#   update gold standard
#cluster the reviews

#evaluate purity
def getGoldStandardReviews():
    reviews = pickle.load(open("data/gameReviewDict.p", "rb"))
    reviewsList = []
    cutoff = 1000
    goodReviews = 0
    badReviews = 0
    for gameSystemKey, systemDict in reviews.items():
        if badReviews > cutoff and goodReviews > cutoff:
            break
        for gameKey, gameReview in systemDict.items():
            if badReviews > cutoff and goodReviews > cutoff:
                break
            if "review" in gameReview and "scores" in gameReview and "gamespot score" in gameReview["scores"]:
                if gameReview["scores"]["gamespot score"] < 6 and badReviews <= cutoff:
                    reviewsList.append((gameKey, gameSystemKey, gameReview))
                    badReviews += 1
                if gameReview["scores"]["gamespot score"] >= 6 and goodReviews <= cutoff:
                    reviewsList.append((gameKey, gameSystemKey, gameReview))
                    goodReviews += 1 
    print(badReviews)
    print(goodReviews)
    return reviewsList 

