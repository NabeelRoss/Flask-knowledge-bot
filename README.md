# Flask Knowledge Bot

A smart, lightweight conversational agent built with **Flask** and **Python**. This chatbot uses fuzzy string matching to answer user questions from a JSON knowledge base and features a modern, responsive chat interface.

## 🌟 Features

* **Intelligent Matching:** Uses Python's `difflib` to find the closest matching question, allowing it to understand queries even with typos or slight variations.
* **JSON Knowledge Base:** Stores data in a simple, human-readable `knowledge_base.json` file, making it easy to edit or expand without a database server.
* **Modern UI:** A fully responsive chat interface featuring:
    * WhatsApp-style chat bubbles.
    * Real-time "typing" animations.
    * Auto-scrolling message history.
* **RESTful API:** The backend serves answers via JSON endpoints, separating logic from presentation.

## 📂 Project Structure

```text
flask-knowledge-bot/
│
├── app.py                  # Main Flask application and logic
├── knowledge_base.json     # The "brain" containing questions & answers
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
└── templates/
    └── index.html          # Modern HTML5/CSS3 chat interface
