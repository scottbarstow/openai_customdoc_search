# Open AI and Custom PDF document search demo

This project uses OpenAI, Langchain and Streamlit to demonstrate a 
working website where you can upload PDFs, have the vectors populated, and
then do a semantic search of the contents.

It uses the FAISS in-memory data store for vector storage

## To run the demo

```
pip install openai
pip install langchain
pip install PyPDF2
pip install faiss-cpu
pip install streamlit
pip install tiktoken
```

Next, you'll need to have your OpenAI API Key available. This can be either an environment variable `OPENAI_API_KEY` or 
it will look for the key in a file in your home directory called `openai-api-key.txt`

### Running the Streamlit app

```
streamlit run site.py
```

### Running the console app
Note that you'll need to update the document name and the query with your specific info
```
python main.py
```