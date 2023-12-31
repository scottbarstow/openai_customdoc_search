# Open AI and Custom PDF document search demo

This project uses OpenAI, Langchain and Streamlit to demonstrate a 
working website where you can upload PDFs, have the vectors populated, and
then do a semantic search of the contents.

It uses different data stores for vector storage depending on configuration.

Requires Python 3.10 or later

## To run the demo

```
pip install openai
pip install langchain
pip install PyPDF2
pip install faiss-cpu
pip install chromadb
pip install streamlit
pip install tiktoken
```

Next, you'll need to have your OpenAI API Key available. This can be either an environment variable `OPENAI_API_KEY` or 
it will look for the key in a file in your home directory called `openai-api-key.txt`

### Configuring the Streamlit app
```
cp .streamlit/config.toml.example .streamlit/config.toml
cp src/pdfbotsearch/config.ini.example src/pdfbotsearch/config.ini
```
Then make changes to your local copy

### Running the Streamlit app

```
streamlit run src/pdfbotsearch/site.py
```

### Running the console app
Note that you'll need to update the document name and the query with your specific info
```
python src/main.py
```
