"""Occurrence count is a good start but there is an issue: longer documents will have higher
average count values than shorter documents, even though they might talk about the same topics.
To avoid these potential discrepancies it suffices to divide the number of occurrences of each
word in a document by the total number of words in the document: these new features are called tf for Term Frequencies.
Another refinement on top of tf is to downscale weights for words that occur in many documents
in the corpus and are therefore less informative than those that occur only in a smaller portion of the corpus.
This downscaling is called tf–idf for “Term Frequency times Inverse Document Frequency”."""
from sklearn.feature_extraction.text import TfidfTransformer

""" Text preprocessing, tokenizing and filtering of stopwords are all included in CountVectorizer, 
which builds a dictionary of features and transforms documents to feature vectors."""
from sklearn.feature_extraction.text import CountVectorizer

"""Now that we have our features, we can train a classifier to try to predict the category of a 
post. Let’s start with a naïve Bayes classifier, which provides a nice baseline for this task. 
scikit-learn includes several variants of this classifier; the one most suitable for word counts 
is the multinomial variant."""
from sklearn.naive_bayes import MultinomialNB

"""linear support vector machine (SVM), which is widely regarded as one of the best text 
classification algorithms (although it’s also a bit slower than naïve Bayes)."""
from sklearn.linear_model import SGDClassifier

"""COMMENT TODO"""
from sklearn.neural_network import MLPClassifier

"""In order to make the vectorizer => transformer => classifier easier to work with, 
scikit-learn provides a Pipeline class"""
from sklearn.pipeline import Pipeline

import pandas as pd
import sys


def main():
    # loading dataset
    data_set_path = "../res/Emotions.csv"
    testing_set_path = "../res/Testingdata.csv"
    dataset = pd.read_csv(data_set_path, header=0, sep=",", names=["Statement", "Emotion"], encoding='cp1252')
    testset = pd.read_csv(testing_set_path, header=0, sep=",", names=["Statement", "Emotion"], encoding='cp1252')

    """feature engineering"""

    # creating bag of words
    count_vect = CountVectorizer()
    bag = count_vect.fit_transform(dataset)

    tf_transformer = TfidfTransformer(use_idf=False).fit(bag)
    X_train_tf = tf_transformer.transform(bag)

    #clf = MultinomialNB().fit(X_train_tf, twenty_train.target) TODO


if __name__ == '__main__':
    sys.exit(main())
