from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Initialize the OpenAI API (replace with your own API key)
openai.api_key = "your-openai-api-key"

@app.route('/api/gpt4', methods=['POST'])
def gpt4():
    try:
        # Extract the input text from the request
        data = request.json
        prompt = data.get('prompt', '')

        # Generate a response from the GPT-4 model
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are ChatGPT, a large language model."},
                {"role": "user", "content": prompt}
            ]
        )

        # Return the response
        return jsonify(response.choices[0].message["content"])
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
