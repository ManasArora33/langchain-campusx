from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of WB",
    "Paris is the capital of France"
]

text = "India capital is delhi"

vector = embedding.embed_query(text)  

print(str(vector))