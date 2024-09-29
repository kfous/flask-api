import torch
from transformers import pipeline


def sentiment_result(transcript):
    model_id = 'siebert/sentiment-roberta-large-english'
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    # Sentiment
    pipe = pipeline(
        "sentiment-analysis",
        model=model_id,
        top_k=None,
        device=device
    )

    result = pipe(transcript)
    return result[0]


def model_pipeline():
    model_id = 'siebert/sentiment-roberta-large-english'
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    # Sentiment
    pipe = pipeline(
        "sentiment-analysis",
        model=model_id,
        top_k=None,
        device=device
    )

    return pipe