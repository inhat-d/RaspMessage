from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

OPEN_AI_KEY = os.environ['openAI_key']

client = openai.OpenAI(api_key=OPEN_AI_KEY)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = process_prompt(prompt)
        return render_template('index.html', answer=response)
    else:
        return render_template('index.html')

@app.route('/chatgpt', methods=['POST'])
def chatgpt_route():
    data = request.get_json()
    prompt = data.get('prompt')
    if prompt:
        response = process_prompt(prompt)
        return jsonify({'answer': response})
    else:
        return jsonify({'error': 'Missing prompt'}), 400

def process_prompt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)
