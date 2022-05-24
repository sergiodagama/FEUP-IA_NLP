def classifier(method: str):
    if method == "Naive Bayes":
        return naiveBayes()
    elif method == "Linear SVM":
        return linearSVM()
    elif method == "Decision Tree":
        return decisionTree()
    elif method == "Neural Network":
        return neuralNetwork()
    else:
        print('Unknown method name')
        return -1


def naiveBayes():
    return 0


def linearSVM():
    return 0


def decisionTree():
    return 0


def neuralNetwork():
    return 0
