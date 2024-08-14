

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import elastic_vector_search,pinecone,weaviate,faiss
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import openai
import os
os.environ['OPENAI_API_KEY'] = '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'
chemin_pdf = r"C:\Users\Admin\Desktop\EtE2024\projet_final_rcw\maladie_prevention.pdf"
def extract_pdf():
    with open(chemin_pdf, "rb") as fichier_pdf:
        reader=PdfReader(fichier_pdf)
        raw_text=''
        for i,page in enumerate(reader.pages):
            text=page.extract_text()
            if text:
                raw_text+=text
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = splitter.split_text(raw_text)
    return chunks

def create_vectorstore():
    chunks=extract_pdf()
    current_embedding = OpenAIEmbeddings()
    vectorestore = faiss.from_texts(texts=chunks, embedding=current_embedding)
    return vectorestore

def generate(input_user):
    chain=load_qa_chain(openai(),chain_type="stuff")
    docsearch=create_vectorstore()
    docs=docsearch.similarity_search(input_user)
    response=chain.run(input_documents=docs,question=input_user)
    return response
extract_pdf()