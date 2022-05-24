def preProcessingIf():
    pass


def preProcessingIfIdf():
    pass


def preProcessing(method: str):
    if method == "if":
        return preProcessingIf()
    if method == "if":
        return preProcessingIfIdf()
    if method == "if":
        return preProcessingBagOfWords()