from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain

# .envファイルをロード
load_dotenv()

# .envファイルから変数を読み込む
openai_api_key = os.getenv('OPENAI_API_KEY')

template = """質問に合わせた適切な検索ワードをひとつ提案してください。
質問: {question}
検索ワード:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo")

question = "ぼっち・ざ・ろっくのぼっちちゃんの本名は？"

llm_chain = LLMChain(prompt=prompt, llm=llm)

result = llm_chain.run(question)
print(result)
