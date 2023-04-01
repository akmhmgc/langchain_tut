from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.utilities import SerpAPIWrapper

# .envファイルをロード
load_dotenv()

# .envファイルから変数を読み込む
openai_api_key = os.getenv('OPENAI_API_KEY')
os.environ["SERPAPI_API_KEY"] = os.getenv('SERPAPI_API_KEY')

def multiplier(a, b):
    return a * b

def parsing_multiplier(string):
    a, b = string.split(",")
    return multiplier(int(a), int(b))

llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
search = SerpAPIWrapper()

description = (
  "This tool is useful for when you need to multiply two numbers together. ",
  "The input to this tool should be a comma separated list of numbers of length two, ",
  "representing the two numbers you want to multiply together. ",
  "For example, `1,2` would be the input if you wanted to multiply 1 by 2."
)
tools = [
    Tool(
        name = "Multiplier",
        func=parsing_multiplier,
        description="".join(description)
    ),
        Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search"
    )
]
mrkl = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

mrkl.run("富士山の高さに10をかけた値を教えてください。")
