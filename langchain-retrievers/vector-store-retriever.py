from langchain_chroma import Chroma
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=NVIDIAEmbeddings(),
    collection_name='my_collection',
    ids=[f"id_{i}" for i in range(len(documents))]
    
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2}
)

query = "What is Chroma?"
result = retriever.invoke(query)

for doc in result:
    print(f"Content: {doc.page_content}")
    