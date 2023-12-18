from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.utilities.dalle_image_generator import DallEAPIWrapper

from fastapi import FastAPI
from langserve import add_routes

openai_key = "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"

llm = OpenAI(temperature=0.5, openai_api_key=openai_key)
prompt = PromptTemplate(
    input_variables=["image_desc"],
    template="Generate a detailed prompt to generate a hyperrealistic photographic image based on the following description: {image_desc}",
)
chain = LLMChain(llm=llm, prompt=prompt)

image_url = DallEAPIWrapper().run(chain.run("wizard smoking a joint"))
print(image_url)

"""
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
    """