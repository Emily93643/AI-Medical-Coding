from sentence_transformers import SentenceTransformer
from qdrant_client import models, QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
import time

def get_coded_term(dict="meddra26.1", term="", top_k=1):

    model = SentenceTransformer('./model/all-MiniLM-EV34-L6-v2')
    client = QdrantClient("http://localhost:6333")

    dict_name = dict[:6]
    dict_version = float(dict[6:10])
    
    # Constructing Filter with FieldCondition
    query_filter =Filter(
        must=[
#            FieldCondition(
#                key="pt_name", match=MatchValue(value="Pain")
#             )
             FieldCondition(
                key="vernum", range=models.Range(
                                           gt=None,
                                           gte=dict_version,
                                           lt=None,
                                           lte=dict_version,
                                           )
            )
        ]
    )
    #MedDRA any version: meddra0
    if dict_version == 0:
       query_filter=None 

    # Perform search
    response = client.search(
        collection_name=dict_name,
        query_filter=query_filter,
        query_vector=model.encode(term).tolist(),
        limit=100,
    )

    #print(response)
    # Process response
    result_arr = []
    for result in response:
        result.payload['term']=term
        result.payload['score']=result.score
        result_arr.append(result.payload) 

    return result_arr
    
if __name__ == "__main__":
    print("\n*** Get Current Coded Term ***\n")
          
    dict = input("\nPlease enter a dict/version: ")

    dict_name = dict[:6]
    dict_version = float(dict[6:10])
    

    print(dict_name, dict_version)



    term = input("\nPlease enter a term name: ")

    # #Check for empty strings/ only spaces
    # if not bool(city.strip()):
    #     city = "Toronto"
    t_start=time.perf_counter()
    coding_data = get_coded_term(dict, term)
    t_stop=time.perf_counter()
    print("Elapsed time in seconds:",t_stop-t_start)
   
    #print("\n")
    print(coding_data)
    # print("Shape of DataFrame:\n", coding_data.shape)
    #print("Column Names:\n", coding_data.columns.tolist())
    #print("Data Types of Columns:\n", coding_data.dtypes)