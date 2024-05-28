import matplotlib.pyplot as plt
import numpy as np
from arguments import args
from analyzer import Analyzer

def plot_sentiment(sentiment, percentage):
    labels = ['Negative', 'Positive']
    probabilities = [percentage, 100 - percentage] if sentiment == 'Negative' else [100 - percentage, percentage]
    colors = ['red', 'green']
    
    plt.figure(figsize=(6, 4))
    plt.bar(labels, probabilities, color=colors)
    plt.title(f"Sentiment Analysis Result: {sentiment} ({percentage}%)")
    plt.xlabel('Sentiment')
    plt.ylabel('Probability')
    plt.ylim(0, 100)
    plt.show()

if __name__ == "__main__":
    print("Please hold on while the analyzer is being prepared for use...")

    analyzer = Analyzer(will_train=False, args=args)

    text = input("Please provide the text you'd like to have analyzed for sentiment: ")

    while text:
        sentiment, percentage = analyzer.classify_sentiment(text)
        print(f"The {sentiment} sentiment with a probability of {percentage}% .")
        plot_sentiment(sentiment, percentage)
        text = input("Please enter the sentiment you wish to analyze: ")
