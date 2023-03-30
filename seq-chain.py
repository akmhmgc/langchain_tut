from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

# .envファイルをロード
load_dotenv()

# LLMの準備
llm = OpenAI(temperature=.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

# テンプレートの準備
template = """あなたは劇作家です。劇のタイトルが与えられた場合、そのタイトルのあらすじを書くのがあなたの仕事です。

タイトル:{title}
あらすじ:"""

# プロンプトテンプレートの準備
prompt_template = PromptTemplate(
    input_variables=["title"], 
    template=template
)

synopsis_chain = LLMChain(llm=llm, prompt=prompt_template)


# テンプレートの準備
template = """あなたは演劇評論家です。 劇のあらすじが与えられた場合、そのあらすじのレビューを書くのがあなたの仕事です。

あらすじ:
{synopsis}
レビュー:"""

# プロンプトテンプレートの準備
prompt_template = PromptTemplate(
    input_variables=["synopsis"], 
    template=template
)

# LLMChainの準備
review_chain = LLMChain(llm=llm, prompt=prompt_template)

overall_chain = SimpleSequentialChain(
    chains=[synopsis_chain, review_chain], 
    verbose=True
)

review = overall_chain.run("大きな猿の一生")

print(review)
