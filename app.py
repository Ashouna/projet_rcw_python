from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import create, login, update_patient 
from classification import classification
from PyPDF2 import PdfReader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Activez CORS pour votre application Flask

os.environ['OPENAI_API_KEY'] = 'sk-proj-8vaEYbanlDuLslQzMVBuT3BlbkFJ8wi3jbdXQwKJ9fRQEfmc'
chemin_pdf = r"C:\Users\Admin\Desktop\EtE2024\projet_final_rcw\maladie_prevention.pdf"

def extract_pdf():
    with open(chemin_pdf, "rb") as fichier_pdf:
        reader = PdfReader(fichier_pdf)
        raw_text = ''
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                raw_text += text

    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = splitter.split_text(raw_text)
    return chunks

def create_vectorstore():
    chunks = extract_pdf()
    current_embedding = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=current_embedding)
    return vectorstore

def generate(input_user):
    chain = load_qa_chain(ChatOpenAI(), chain_type="stuff")
    docsearch = create_vectorstore()
    docs = docsearch.similarity_search(input_user)
    response = chain.run(input_documents=docs, question=input_user)
    return response

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_input = data['user_input']
    output = generate(user_input)
    return jsonify({'response': output})

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    res = create(data)
    response = {'success': 'False'} if res else {'success': 'True'}
    return jsonify(response)

@app.route('/api/login', methods=['POST'])
def Login():
    data = request.get_json()
    user, res = login(data)
    response = {'success': 'True', 'data': user} if res else {'success': 'False', 'data': None}
    return jsonify(response)

@app.route('/api/modif', methods=['POST'])
def Modif():
    data = request.get_json()
    res = update_patient(data)
    response = {'success': 'True', 'msg': 'Informations mises à jour avec succès'} if res else {'success': 'False', 'msg': 'Impossible de faire la mise à jour avec succès'}
    return jsonify(response)


@app.route('/api/prediction', methods=['POST'])
def predict_patient():
    data = request.get_json()
    resultat = classification(data)
    response = {'success': 'True', 'data': resultat}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
