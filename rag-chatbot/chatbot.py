from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA,NVIDIAEmbeddings
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatNVIDIA(model='openai/gpt-oss-120b')

# 1. Indexing

# loader
video_id = "gVGhTX0g5LI"
try:
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.fetch(video_id=video_id)
    transcript_list_json = transcript_list.to_raw_data()
    transcript = " ".join(chunk['text'] for chunk in transcript_list_json)
    # print(transcript)
    # print(transcript_list.to_raw_data())
except TranscriptsDisabled:
    print("No captions available for this video")

# text-splitter 
splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
chunks = splitter.create_documents([transcript])
# print(len(chunks))
# print(chunks[0])

# vector store
embeddings = NVIDIAEmbeddings(model = 'nvidia/nv-embed-v1')
vector_store = Chroma.from_documents(chunks,embedding=embeddings,collection_name='youtube_transcript')
# print(vector_store.get(include=['documents']))

# 2. Retrieval
retriever = vector_store.as_retriever(search_type='similarity',search_kwargs={'k':4})
# result = retriever.invoke('Is an asteroid going to destroy earth')

# for doc in result:
    # print(f"Content: {doc.page_content}")
    # print("-" * 30)

# 3. Augmentation
prompt = PromptTemplate(
    template = """
    You are a helpful assistant , Answer only from the provided youtube transcript context, if the context is insufficient just say you don't know.
    {context}
    Question: {question}
    """
    ,
    input_variables = ['context','question']
)

question = 'Is an asteroid going to destroy earth'
retrieved_docs = retriever.invoke(question)

context_text = "\n\n".join([doc.page_content for doc in retrieved_docs])
# print(context_text)
final_prompt = prompt.invoke({'context':context_text,'question':question})

# print(final_prompt)

# # 4. Generation
# result = model.invoke(final_prompt)
# print(result.content)

# now we will perform the same process by forming a chain
def format_docs(retrieved_docs):
    return "\n\n".join([doc.page_content for doc in retrieved_docs])

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})
# print(parallel_chain.invoke('Is an asteroid going to destroy earth'))
parser = StrOutputParser()
simple_chain = prompt | model | parser

final_chain = parallel_chain | simple_chain
result = final_chain.invoke('when will the closest asteroid pass through earth')
print(result)

