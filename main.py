## This is a simple prototype of using Langchain on a PDF document to search it. 
## The site.py is a more fulsome, realtime example of using Langchain to search a PDF document.

import os

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from openai_utils import get_openai_api_key
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI


reader = PdfReader("/home/jean/AI/courses/prompt_engineering/ai-sandbox-pdf/2106.09685.pdf")

raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

text_splitter = CharacterTextSplitter(        
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)
print(len(texts))

openai_api_key = get_openai_api_key()
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

docsearch = FAISS.from_texts(texts, embeddings)

chain = load_qa_chain(OpenAI(openai_api_key=openai_api_key), chain_type="stuff")

query = "what does LoRA means ?"
docs = docsearch.similarity_search(query)
print(chain.run(input_documents=docs, question=query))
