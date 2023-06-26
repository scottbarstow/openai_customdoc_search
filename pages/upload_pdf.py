import streamlit as st
from langchain import OpenAI
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from openai_utils import get_openai_api_key
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

st.markdown("# PL DocuBot")
st.sidebar.markdown("# Upload a Document")

def get_raw_text(reader):
    raw_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text
    return raw_text

def get_texts(raw_text):
    text_splitter = CharacterTextSplitter(        
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap  = 200,
        length_function = len,
    )
    texts = text_splitter.split_text(raw_text)
    return texts


def populate_vector_store(texts, embeddings):
    vector_store = FAISS.from_texts(texts, embeddings)
    return vector_store


def generate_response(input_text, vector_store):
    chain = load_qa_chain(OpenAI(openai_api_key=openai_api_key), chain_type="stuff")
    docs = vector_store.similarity_search(input_text)
    st.info(chain.run(input_documents=docs, question=input_text))


uploaded_file = st.file_uploader("Choose a PDF file")
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    st.info("Processing file")
    raw_text = get_raw_text(reader)
    texts = get_texts(raw_text)
    openai_api_key = get_openai_api_key()
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vector_store = populate_vector_store(texts, embeddings)

    with st.form('my_form'):
        text = st.text_area('Prompt:', '', placeholder='Ask LakeBot anything about HPPO')
        submit = st.form_submit_button('Go')

        if submit:
            generate_response(text, vector_store)



