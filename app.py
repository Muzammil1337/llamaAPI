from flask import Flask, request, jsonify
from flask_cors import CORS
from gradio_client import Client

app = Flask(__name__)
CORS(app)

client = Client("Be-Bo/llama-3-chatbot_70b")

@app.route('/', methods=['GET'])
def get_index():
    return "Hello World"

@app.route('/process', methods=['POST'])
def process_prompt():
    data = request.json
    if 'prompt' not in data:
        return jsonify({"error": "No prompt provided"}), 400
    
    prompt = data['prompt']
    result = client.predict(
        message=prompt,
        api_name="/chat"
    )
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
