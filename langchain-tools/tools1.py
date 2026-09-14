# from langchain_community.tools import DuckDuckGoSearchRun

# search_tool = DuckDuckGoSearchRun()

# result = search_tool.invoke("what is the geopolitical news today india")

# print(result)

from langchain.agents import create_agent
from langchain.agents.middleware import ShellToolMiddleware, HostExecutionPolicy
from langchain_core.messages import HumanMessage
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
from langchain_community.tools import ShellTool
load_dotenv()

model = ChatNVIDIA(model="openai/gpt-oss-20b", max_completion_tokens=1000)
shell_tool = ShellTool()
# agent = create_agent(
#     model=model,
#     tools=[],
#     middleware=[
#         ShellToolMiddleware(
#             workspace_root=r"D:\langchain-tools",
#             shell_command=["powershell.exe", "-NoProfile", "-Command"],
#             execution_policy=HostExecutionPolicy(),
#         ),
#     ],
# )

# result = agent.invoke(
#     {"messages": [HumanMessage(content="Run: pwd Return the output only.")]}
# )


# result = model.invoke("who is the current president of the United States?")

result = shell_tool.invoke("whoami")
print(result)
print('PATCH APPLIED')