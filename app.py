from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de um banco de dados ou lista de respostas     ---- EDITAR INFORMAÇÕES ----
farmacia_info = {
    "horario": "Nosso horário de funcionamento é de segunda a sábado, das 8h às 18h.",
    "entrega": "Fazemos entregas em toda a cidade. A taxa varia conforme a sua localização.",
    "produtos": "Temos uma grande variedade de produtos, de medicamentos a produtos de higiene pessoal. Qual produto você procura?"
}

# Rota principal para o N8N enviar as mensagens
@app.route('/atendente', methods=['POST'])
def atendente():
    data = request.json
    user_message = data.get('message', '').lower() # Pega a mensagem e a converte para minúsculas

    # Lógica de negócio da farmácia
    if any(keyword in user_message for keyword in ["horario", "horas", "abre", "fecha"]):
        return jsonify({
            "response": farmacia_info["horario"],
            "action": "respond_directly"
        })
    elif "entrega" in user_message:
        return jsonify({
            "response": farmacia_info["entrega"],
            "action": "respond_directly"
        })
    elif any(keyword in user_message for keyword in ["produto", "remedio", "medicamento"]):
        return jsonify({
            "response": farmacia_info["produtos"],
            "action": "respond_directly"
        })
    else:
        # Se a mensagem não se encaixar em nenhuma regra, indica que o N8N deve usar a IA
        return jsonify({
            "response": "Pergunta não identificada.",
            "action": "pass_to_ai"
        })

# Rota de teste para verificar se a API está online
@app.route('/', methods=['GET'])
def home():
    return "API do Atendente de Farmácia está online!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)