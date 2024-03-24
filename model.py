import time
t_start=time.perf_counter()
from sentence_transformers import SentenceTransformer
from qdrant_client import models, QdrantClient
import pandas as pd

df = pd.read_csv(r".\dict\meddra26_1.csv")
documents = df.to_dict(orient="records")

encoder = SentenceTransformer('./model/all-MiniLM-EV34-L6-v2')
qdrant = QdrantClient("http://localhost:6333")
qdrant.recreate_collection(
    collection_name="my_books",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)

qdrant.upload_points(
    collection_name="my_books",
    points=[
        models.PointStruct(
            id=idx, vector=encoder.encode(doc["llt_name"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)

hits = qdrant.search(
    collection_name="my_books",
    query_vector=encoder.encode("pain").tolist(),
    limit=3,
)

for hit in hits:
    print(hit.payload, "score:", hit.score)

t_stop=time.perf_counter()
print("Elapsed time in seconds:",t_stop-t_start)

