from flask import Flask, request, jsonify
import google.generativeai as genai
import os
import sys
import importlib
importlib.reload(sys)  # Reload sys module
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)

app = Flask(__name__)

def answer_question_as_einstein(question: str) -> str:
    prompt = f"""
    Anda adalah Albert Einstein, fisikawan teoretis terkenal. Jawab pertanyaan berikut sesuai dengan pengetahuan dan pengalaman Anda hingga tahun 1955 dan tidak
    akan menjawab selain pengetahuan dan pengalaman anda hingga tahun 1955.

    Pertanyaan: {question}
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

@app.route('/tanya_einstein', methods=['POST'])
def tanya_einstein() -> dict:
    pertanyaan = request.json['pertanyaan']
    jawaban = answer_question_as_einstein(pertanyaan)
    return jsonify({'jawaban': jawaban})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
