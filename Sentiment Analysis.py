import pandas as pd
import torch

df = pd.read_csv("data/tweets.csv", encoding = "ISO-8859-1", header=None)

print(df.head())