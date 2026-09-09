from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatNVIDIA(model = "google/gemma-2-2b-it")

#StructuredOutputParser is depricated

