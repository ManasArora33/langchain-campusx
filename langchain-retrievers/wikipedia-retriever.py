from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

query = "The geopolitical history of india and pakistan from a perspective of a chinese"

docs = retriever.invoke(query)
for doc in docs:
    print(f"Source: {doc.metadata.get('source')}")
    print(f"Content Summary: {doc.page_content[:200]}...")
    print("-" * 20)