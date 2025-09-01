------------------ MANUAL ------------------

## O que o Código Faz??
farmacia_info: Este dicionário simula um pequeno banco de dados. Você pode facilmente expandir isso para se conectar a um banco de dados real ou a outra API de estoque.

Análise da mensagem: O código verifica se a mensagem do cliente contém palavras-chave como "horario", "entrega" ou "produto".

Resposta condicionada:

Se uma palavra-chave é encontrada, a API retorna uma resposta específica da farmácia junto com a instrução "action": "respond_directly".

Se nenhuma palavra-chave é encontrada, a API retorna a instrução "action": "pass_to_ai"


## What that Code does?
- farmácia_info: This dictionary simulates a small database. You can easily expand this to connect to a real database or another inventory API.

- Message parsing: The code checks if the customer's message contains keywords like "horário," "entrega," or "produto."

- Conditional response:

If a keyword is found, the API returns a pharmacy-specific response along with the "action" instruction: "respond_directly."

If no keyword is found, the API returns the "action" instruction: "pass_to_ai."


Start Command for Render:
gunicorn --bind 0.0.0.0:8000 app:app