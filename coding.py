from sentence_transformers import SentenceTransformer, util
import pandas as pd
import time

def get_coded_term(dict="MedDRA", version="26.1", term="", top_k=1):

    model = SentenceTransformer('./model/all-MiniLM-EV34-L6-v2')

    #Emebdding
    df = pd.read_pickle(r".\dict\meddra26_1_llt_embeddings_EV34.pkl")
    
    term_list=[term]
    q_Embeddings=model.encode(term_list, convert_to_tensor=True) 
    df['Cos_Sim']=df.apply(lambda x: util.pytorch_cos_sim(x['LLT_Embeddings'], q_Embeddings).data[0,0].numpy(), axis=1).tolist()
    #coding_data = df.sort_values('Cos_Sim',ascending = False).groupby('term').head(1)
    coding_key = df.sort_values('Cos_Sim',ascending = False).head(100)
    coding_key['term']=term

    dict = pd.read_csv(r".\dict\meddra26_1.csv")
    coding_data = pd.merge(coding_key[['term', 'llt_code', 'Cos_Sim']], dict, on='llt_code', how='left')
    
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
    print("Shape of DataFrame:\n", coding_data.shape)
    #print("Column Names:\n", coding_data.columns.tolist())
    #print("Data Types of Columns:\n", coding_data.dtypes)