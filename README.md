Our code has the following dependencies:
Python 3.4
NLTK 3
Scikit-Learn http://scikit-learn.org/stable/install.html#install-by-distribution
AlchemyAPI for python http://www.alchemyapi.com/developers/getting-started-guide/using-alchemyapi-with-python
MatPlotLib for python http://matplotlib.org/
The DePaul University Researchers' GameSpot Corpus https://www.dropbox.com/s/0sxz6yk4sh89il6/games.zip?dl=0


This project performs real-time sentiment classification of video game reviews, as well as clustering of video game reviews into related groups. Our corpus was provided to us by Kevin Raison, Noriko Tomuro, and Steve Lytinen. You can find their work at www.academia.edu/download/30186920/japtal2012.pdf.

First, either git clone the project repo from https://github.com/JustinRoll/480_GameReview_Datamining if you don't already have the code.

Next, you will need to install all of the dependent code. For AlchemyApi, you will need to download the AlchemyAPI python library (see link above) and register a key. You will need to copy alchemyapi.py to this project's source directory, then run python3 alchemyapi.py YOURKEYHERE.

You will then need to make a data directory. So mkdir data in this project's directory. Extract the games.zip corpus into it, so under data you should have a directory called Gamespot-Cleaned. There will be many text files arranged like this: data/Gamespot-Cleaned/Playstation/reviewname.txt
There are about 700 megs of reviews, so make sure you have space.

Once you have all the data, you will need to run the parser on the corpus. This will parse all the reviews in the dictionary. This can be run by typing python3 parser.py. You should now have a pickled dictionary called gameReviewDict.p in the root of the project directory. You will then need to run the classifier. It can be run from the terminal by typing
python3 reviewDriver.py. Once this finishes, you will now have a reviewclassifier.p file in the project root, and you should also see the 5-fold accuracy of the classifier printed out.

You will now be able to run the gui by typing pythone gui.py into the terminal.

The clusterer can be run manually by typing one of the below commands into the shell: 

python3 clusterEvaluation.py kmeans tfidf
python3 clusterEvaluation.py kmeans wc
python3 clusterEvaluation.py kmeans entity
python3 clusterEvaluation.py dbscan tfidf
python3 clusterEvaluation.py dbscan wc
python3 clusterEvaluation.py dbscan entity

The first parameter is the type of clustering algorithm, while the second parameter is the type of features to use.
