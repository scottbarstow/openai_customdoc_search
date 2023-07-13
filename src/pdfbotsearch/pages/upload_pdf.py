import streamlit as st
from langchain import OpenAI
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from openai_utils import get_openai_api_key
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from components.PDFVectorStore import PDFVectorStore
from components.PDFVectorStoreEnum import PDFVectorStoreEnum
from components.PDFExtractor import PDFExtractor
from components.PDFExtractorEnum import PDFExtractorEnum
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

st.markdown("# The PDF DocuBot")
st.sidebar.markdown("# Upload a Document")
openai_api_key = get_openai_api_key()
# Create the Vectorstore
pdfVectorStore = PDFVectorStore(openai_api_key=openai_api_key,store_type=PDFVectorStoreEnum.Chroma)


def generate_response(query, vector_store):
    # Creates the Chain
    llm = ChatOpenAI(temperature = 0.0, openai_api_key=openai_api_key)
    # use either stuff, map_reduce or refine as chain type to experiment with different approaches
    qa_stuff = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", # map_reduce, refine, map_rerank are other options
        retriever=pdfVectorStore.get_retriever(), 
        verbose=True
    )

    # query ="Can you please list and summarize each section of the 2106.09685 PDF \
    # in a table in markdown with the first column being the section title and the second one being the summary of the section."    
    st.info(qa_stuff.run(query))
    
    # chain = load_qa_chain(OpenAI(openai_api_key=openai_api_key), chain_type="stuff")
    # docs = vector_store.similarity_search(input_text)
    # st.info(chain.run(input_documents=docs, question=input_text))


uploaded_file = st.file_uploader("Choose a PDF file")
if uploaded_file is not None:

    #file_path = '/home/jean/AI/courses/prompt_engineering/ai-sandbox-pdf/1706.03762.pdf'
    #file_path = 'https://arxiv.org/pdf/1706.03762.pdf'
    # load the PDF file and extract it to docs
    docs = PDFExtractor.extract_docs_from_PDF(uploaded_file, PDFExtractorEnum.PdfReader)
    st.info("extracted PDF to OpenAI docs " + str(len(docs)))
    # Add new docs to the Vectorstore
    pdfVectorStore.populate_db(docs)
    st.info("populated Docs to Vector Store DB")
    
    with st.form('my_form'):
        text = st.text_area('Prompt:', '', placeholder='Ask LakeBot anything about HPPO')
        submit = st.form_submit_button('Go')

        if submit:
            generate_response(text, pdfVectorStore)



