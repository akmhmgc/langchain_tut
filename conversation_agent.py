from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, Tool
from langchain.tools import BaseTool
from langchain.utilities import SerpAPIWrapper
from langchain.agents import AgentType

# .envファイルをロード
load_dotenv()

# .envファイルから変数を読み込む
openai_api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo")

class CustomSearchTool(BaseTool):
    name = "ImageGenerator"
    description = "useful for generating image URL"

    def _run(self, query: str) -> str:
        """Use the tool."""
        return 'http://hoge.image.com'

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")


serapi_api_key = os.getenv('SERPAPI_API_KEY')
search = SerpAPIWrapper(serpapi_api_key=serapi_api_key)


tools = [CustomSearchTool(), 
          Tool(
                  name = "Search",
                  func=search.run,
                  description="useful for when you need to answer questions about a topic"
              )
    ]


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)

agent.run("te")
