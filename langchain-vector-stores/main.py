from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )

docs = [doc1,doc2,doc3,doc4,doc5]
doc_ids = ["doc1", "doc2", "doc3", "doc4", "doc5"]

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=NVIDIAEmbeddings(),
    persist_directory='chroma_db',
    collection_name='sample',
    ids=doc_ids
)

# print("Total documents in vector store:", len(vector_store.
# get()['ids']))
# print(vector_store.get(include=['embeddings','documents','metadatas']))

# vector_store.add_documents()

# print(vector_store.similarity_search(
#     query='who among these are a bowler',
#     k=1
# ))

# print(vector_store.similarity_search_with_score(
#     query='who among these are a bowler',
#     k=2
# ))

print(vector_store.similarity_search_with_score(
    query="players",
    filter={'team':'Chennai Super Kings'}
))

vector_store.update_document(document_id="doc3",
    document=Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to five IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings", "role": "Captain"}
    )
)

vector_store.delete(ids=["doc5"])