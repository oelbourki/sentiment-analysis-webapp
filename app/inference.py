from os import pipe
import pip
from transformers import pipeline

classifier = pipeline("sentiment-analysis")


# classifier = pipeline
def get_prediction(input: str):
    return classifier(input)