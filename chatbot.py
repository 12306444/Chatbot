from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Set up your Gemini API key
genai.configure(api_key="AIzaSyDqIdrc5Fs7QO5kTVRmA_MrEIjflbJqZRg")

# Load the Gemini model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-8b-latest")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("message")
    try:
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
