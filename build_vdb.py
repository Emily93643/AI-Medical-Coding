from sentence_transformers import SentenceTransformer
from qdrant_client import models, QdrantClient
import pandas as pd
import time

t_start=time.perf_counter()

df230 = pd.read_csv(r".\dict\meddra230.csv")
df231 = pd.read_csv(r".\dict\meddra231.csv")
df240 = pd.read_csv(r".\dict\meddra240.csv")
df241 = pd.read_csv(r".\dict\meddra241.csv")
df250 = pd.read_csv(r".\dict\meddra250.csv")
df251 = pd.read_csv(r".\dict\meddra251.csv")
df260 = pd.read_csv(r".\dict\meddra260.csv")
df261 = pd.read_csv(r".\dict\meddra261.csv")
df=pd.concat([df230, df231, df240, df241, df250, df251, df260, df261], axis=0)

documents = df.to_dict(orient="records")

encoder = SentenceTransformer('./model/all-MiniLM-EV34-L6-v2')
qdrant = QdrantClient("http://localhost:6333")
qdrant.recreate_collection(
    collection_name="meddra",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)

qdrant.upload_points(
    collection_name="meddra",
    points=[
        models.PointStruct(
            id=idx, vector=encoder.encode(doc["llt_name"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)

#test:
hits = qdrant.search(
    collection_name="meddra",
    query_vector=encoder.encode("pain").tolist(),
    limit=3,
)

for hit in hits:
    print(hit.payload, "score:", hit.score)

t_stop=time.perf_counter()
print("Elapsed time in seconds:",t_stop-t_start)
##Elapsed time in seconds: 9982.1099372000##
##Elapsed time in seconds: 9839.679331900003##
