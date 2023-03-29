from dotenv import load_dotenv
import os
from langchain.llms import OpenAI

# .envファイルをロード
load_dotenv()

# .envファイルから変数を読み込む
openai_api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature=0.9, openai_api_key=openai_api_key)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))
