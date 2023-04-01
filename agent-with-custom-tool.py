from dotenv import load_dotenv
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent, Tool
from langchain import OpenAI, SerpAPIWrapper


# .envファイルをロード
load_dotenv()

# .envファイルから変数を読み込む
openai_api_key = os.getenv('OPENAI_API_KEY')
serapi_api_key = os.getenv('SERPAPI_API_KEY')

llm = OpenAI(temperature=0.9, openai_api_key=openai_api_key)


# ツールの準備
params = {
    "engine": "google_scholar",
}
search = SerpAPIWrapper(params=params, serpapi_api_key=serapi_api_key)
tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about a topic"
    )
]

# エージェントの準備
agent = initialize_agent(
    tools, 
    llm, 
    agent="zero-shot-react-description", 
    verbose=True
)

agent.run("腸内改善が改善されるとうつ病が改善される研究結果はありますか？")

