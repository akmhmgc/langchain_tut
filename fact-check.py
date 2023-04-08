from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

# .envファイルをロード
load_dotenv()

# .envファイルから変数を読み込む
openai_api_key = os.getenv('OPENAI_API_KEY')

q = "Will the more financially well-off a family is, the more educated its children will be and the better off they will be in the future?"

llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
template = """{question}\n\n"""
prompt_template = PromptTemplate(input_variables=["question"], template=template)
question_chain = LLMChain(llm=llm, prompt=prompt_template)

# template = """Here is a statement:
# {statement}
# Make a bullet point list of the assumptions you made when producing the above statement.\n\n"""
# prompt_template = PromptTemplate(input_variables=["statement"], template=template)
# assumptions_chain = LLMChain(llm=llm, prompt=prompt_template)

# template = """Here is a bullet point list of assertions:
# {assertions}
# For each assertion, determine whether it is true or false. If it is false, explain why.\n\n"""
# prompt_template = PromptTemplate(input_variables=["assertions"], template=template)
# fact_checker_chain = LLMChain(llm=llm, prompt=prompt_template)

# template = """In light of the above facts, how would you answer the question '{}'""".format(q)
# template = """{facts}\n""" + template
# prompt_template = PromptTemplate(input_variables=["facts"], template=template)
# answer_chain = LLMChain(llm=llm, prompt=prompt_template)

# overall_chain = SimpleSequentialChain(chains=[question_chain, assumptions_chain, fact_checker_chain, answer_chain], verbose=True)

print(q)
# overall_chain.run(q)

result = question_chain.run(q)
print(result)
