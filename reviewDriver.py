import pickle
from reviewClassifier import Classifier

def getAllReviews():
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
    classifier = Classifier(getAllReviews())

    print("Overall Score Average accuracy: %f" % (classifier.getAverages(classifier.classifyOverallReviews)[1]))
""" print("Overall Score Exact rmse: %f, accuracy: %f" % (classifier.getAverages(classifier.classifyOverallReviewsExact)))
    print("Paragraph accuracy: %f" % (classifier.getAverages(classifier.classifyParagraphReviews)[1]))
    print("Paragraph Exact Score rmse: %f, accuracy: %f" % (classifier.getAverages(classifier.classifyParagraphReviewsExact)))
    print("Authorship rmse: %f, accuracy: %f" % (classifier.getAverages(classifier.classifyAuthorshipReviews)))
"""
#    print("Exact Score (0-5) Paragraph rmse: %f, accuracy: %f" % (classifier.classifyParagraphReviewsExact()))
#    print("Overall rmse: %f, accuracy: %f" % (classifier.classifyOverallReviews()))
#    print("Exact Overall rmse: %f, accuracy: %f" % (classifier.classifyOverallReviewsExact()))
#    print("Authorship score: %f" % classifier.classifyAuthorshipReviews())
main() 