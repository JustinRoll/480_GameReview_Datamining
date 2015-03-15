import pickle
from reviewClassifier import Classifier

def getAllReviews():
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

def getUserReviews():
    reviews = pickle.load(open("data/gameReviewDict.p", "rb"))
    reviewsList = []
    for gameSystemKey, systemDict in reviews.items():
        count = 0
        for gameKey, gameReview in systemDict.items():
            count+=1
            if count > 50:#just to reduce sample size
                break
            if "review" in gameReview and "scores" in gameReview and "gamespot score" in gameReview["scores"]:
                reviewsList.append((gameKey, gameSystemKey, gameReview))
    return reviewsList 

def main():
#    classifier = Classifier(getAllReviews())
    reviewList = []
    for review in getAllReviews():
        if review[1].lower() == "gameboyadvance":
            reviewList.append(review[0])

    reviewList = sorted(reviewList)
    for review in reviewList:
        print(review)

#    print("Overall Score Average accuracy: %f" % (classifier.getAverages(classifier.classifyOverallReviews)))
"""
#    print("Exact Score (0-5) Paragraph rmse: %f, accuracy: %f" % (classifier.classifyParagraphReviewsExact()))
#    print("Overall rmse: %f, accuracy: %f" % (classifier.classifyOverallReviews()))
#    print("Exact Overall rmse: %f, accuracy: %f" % (classifier.classifyOverallReviewsExact()))
#    print("Authorship score: %f" % classifier.classifyAuthorshipReviews())
"""
main() 
