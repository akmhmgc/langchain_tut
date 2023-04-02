from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# .envファイルをロード
load_dotenv()

# .envファイルから変数を読み込む
openai_api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(openai_api_key=openai_api_key, streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature=0)
resp = llm("Write me a song about sparkling water.")

print(resp)
