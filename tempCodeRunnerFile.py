from sentence_transformers import SentenceTransformer
from qdrant_client import models, QdrantClient
import pandas as pd

encoder = SentenceTransformer('./model/all-MiniLM-EV34-L6-v2')

df = pd.read_csv(r".\dict\meddra26_1.csv")

document = df.to_dict()
print(document)