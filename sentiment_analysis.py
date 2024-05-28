from analyzer import Analyzer
from arguments import args

analyzer = Analyzer(will_train=False, args=args)

def analyze_sentiment(text):
    sentiment, percentage = analyzer.classify_sentiment(text)
    print(f"The {sentiment} sentiment with a probability of {percentage}%.")
    return sentiment, percentage
