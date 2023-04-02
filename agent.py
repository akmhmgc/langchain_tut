from dotenv import load_dotenv
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# .envファイルをロード
load_dotenv()

# .envファイルから変数を読み込む
openai_api_key = os.getenv('OPENAI_API_KEY')
serapi_api_key = os.getenv('SERPAPI_API_KEY')

llm = OpenAI(temperature=0.9, openai_api_key=openai_api_key)

# ツールの準備
tools = load_tools(["serpapi"], llm=llm)

# エージェントの準備
agent = initialize_agent(
    tools, 
    llm, 
    agent="zero-shot-react-description", 
    verbose=True
)

agent.run("ぼっち・ざ・ろっくのぼっちちゃんの本名は？")
