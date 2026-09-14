from pathlib import Path

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from deepagents.middleware.filesystem import FilesystemMiddleware
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv

load_dotenv()

# Your workspace folder that contains tools1.py
WORKDIR = Path(r"D:\Practice\langchain-campusx\langchain-campusx\langchain-tools")
FILE_TO_PATCH = WORKDIR / "tools1.py"

# Deep Agents virtual filesystem backend rooted at your workspace
backend = FilesystemBackend(root_dir=str(WORKDIR))

# (Optional) ensure the filesystem middleware is enabled and points at the backend
filesystem_middleware = FilesystemMiddleware(backend=backend)

model = ChatNVIDIA(
    model="openai/gpt-oss-20b",
    timeout=120,
    max_retries=2,
)

agent = create_deep_agent(
    model=model,
    middleware=[filesystem_middleware],
    backend=backend,
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "Open /tools1.py and make a small patch: "
                    "1) Find the final part of the file where it prints or returns output, "
                    "2) Add a new line that prints 'PATCH APPLIED'. "
                    "Use edit_file (minimal changes)."
                ),
            }
        ],
        # Note: with FilesystemBackend, files should already be present under root_dir.
        # The agent will access them via its virtual filesystem.
    }
)

# Print agent messages (the actual code update is done via edit_file)
for msg in result.get("messages", []):
    content = getattr(msg, "content", None)
    if content:
        print(content)