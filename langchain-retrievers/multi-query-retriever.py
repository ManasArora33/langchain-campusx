from langchain_chroma import Chroma
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_core.documents import Document
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv

load_dotenv()

all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]

vector_store = Chroma.from_documents(
    documents=all_docs,
    embedding=NVIDIAEmbeddings(model='nvidia/nv-embed-v1'),
    collection_name='multi_query_collection'
)

similarity_retriever = vector_store.as_retriever(
    search_type = 'similarity',
    search_kwargs={"k": 5}
)

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=similarity_retriever,
    llm = ChatNVIDIA(model="openai/gpt-oss-20b")
)

query = "How to improve energy levels and maintain balance"

similarity_results = similarity_retriever.invoke(query)
multiquery_results = multiquery_retriever.invoke(query)

print("--- Similarity Search Results ---")
for doc in similarity_results:
    print(f"Source: {doc.metadata['source']} | Content: {doc.page_content}")

print("\n--- MultiQuery Search Results ---")
for doc in multiquery_results:
    print(f"Source: {doc.metadata['source']} | Content: {doc.page_content}")

