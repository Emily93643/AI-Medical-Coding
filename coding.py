from sentence_transformers import SentenceTransformer, util
from qdrant_client import models, QdrantClient
import pandas as pd
import time

def get_coded_term(dict="MedDRA", version="26.1", term="", top_k=1):

    model = SentenceTransformer('./model/all-MiniLM-EV34-L6-v2')

    qdrant = QdrantClient("http://localhost:6333")
    hits = qdrant.search(
        collection_name="my_books",
        query_vector=model.encode(term).tolist(),
        limit=100,
    )

    hit_arr = []
    for hit in hits:
        hit.payload['term']=term
        hit.payload['score']=hit.score
        hit_arr.append(hit.payload) 

    coding_data = hit_arr

    print(coding_data)

    return coding_data
    
if __name__ == "__main__":
    print("\n*** Get Current Coded Term ***\n")
          
    dict = input("\nPlease enter a dict name: ")
    version = input("\nPlease enter a version name: ")
    term = input("\nPlease enter a term name: ")

    # #Check for empty strings/ only spaces
    # if not bool(city.strip()):
    #     city = "Toronto"
    t_start=time.perf_counter()
    coding_data = get_coded_term(dict, version, term)
    t_stop=time.perf_counter()
    print("Elapsed time in seconds:",t_stop-t_start)
   
    #print("\n")
    #print(coding_data)
    # print("Shape of DataFrame:\n", coding_data.shape)
    #print("Column Names:\n", coding_data.columns.tolist())
    #print("Data Types of Columns:\n", coding_data.dtypes)