from enum import Enum

class PDFVectorStoreEnum(Enum):
    FAISS = 'FAISS'
    InMemory = "in_memory"
    Chroma = "chroma"