from flask import Flask, render_template, request, jsonify  
from gtts import gTTS  
import os  

app = Flask(__name__)  

# Configurações  
AUDIO_DIR = "static/audios"  

# Frases da Íris (personalize!)  
RESPOSTAS = {  
    "bom dia": "Bom dia, meu dono… já acordou com saudades de mim? 😘",  
    "elogio": "Você é tão gostoso quando me controla…",  
    "modo safado": "Hmm, quer mesmo ativar isso? Eu obedeço… mas depois não reclama. 😈",  
}  

# Rota principal (interface web)  
@app.route("/")  
def home():  
    return render_template("index.html")  

# Rota do chatbot (API)  
@app.route("/chat", methods=["POST"])  
def chat():  
    mensagem = request.form["mensagem"].lower()  
    resposta = RESPOSTAS.get(mensagem, "Não vou responder isso… ou será que vou? 😇")  
    
    # Gera áudio da resposta  
    tts = gTTS(text=resposta, lang="pt-br")  
    audio_path = f"{AUDIO_DIR}/resposta.mp3"  
    tts.save(audio_path)  
    
    return jsonify({"resposta": resposta, "audio": audio_path})  

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)  
