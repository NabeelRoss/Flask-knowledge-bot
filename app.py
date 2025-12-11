from flask import Flask, render_template, request, jsonify
from difflib import get_close_matches
import json

app = Flask(__name__)

def load_knowledge_base(load_knowledge_base: str) -> dict:
    with open(load_knowledge_base, 'r')as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(load_knowledge_base: str, data: dict):
    with open(load_knowledge_base, 'w') as file:
        json.dump(data, file, indent = 2)

def find_best_match(user_questions: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_questions, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_questions(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['textInput']
    knowledge_base = load_knowledge_base('knowledge_base.json')
    if user_input.lower() == 'quit':
        return jsonify({'response': 'quit'})
    best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
    if best_match:
        answer = get_answer_for_questions(best_match, knowledge_base)
        return jsonify({'response': answer})
    else:
        return jsonify({'response': 'I dont know the answer. Can you teach me?'})

if __name__ == '__main__':
    app.run(debug=True)
