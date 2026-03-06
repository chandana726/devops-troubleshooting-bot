# DevOps Troubleshooting Bot

A simple DevOps troubleshooting assistant built with **Python and Flask**.
This project helps engineers quickly identify common infrastructure problems and provides basic troubleshooting commands.

The bot works in **two modes**:

* Web-based chatbot using Flask
* Command Line Interface (CLI) chatbot

---

Features

• Web-based chatbot UI
• CLI troubleshooting bot
• 30+ DevOps troubleshooting scenarios
• JSON-based knowledge base
• Chat interface with welcome message
• Clear chat button to reset conversation
• Lightweight and easy to extend

---

# Project Structure

```
devops-troubleshooting-bot
│
├── app.py             # Flask web server
├── bot.py             # CLI troubleshooting bot
├── knowledge.json     # DevOps troubleshooting knowledge base
├── requirements.txt   # Project dependencies
├── templates
│   └── index.html     # Web interface
└── README.md
```

---

# How the Bot Works

1. The bot loads troubleshooting data from **knowledge.json**.
2. When a user asks a question:

   * The bot searches for matching keywords.
   * If a match is found, it returns the recommended troubleshooting command.
3. If no match is found, the bot returns a fallback response.

---

# Supported Troubleshooting Issues

The bot currently supports 30+ issues 

More troubleshooting cases can be easily added to **knowledge.json**.

---

# Installation

Clone the repository:

```
git clone https://github.com/chandana726/devops-troubleshooting-bot.git
```

Navigate into the project directory:

```
cd devops-troubleshooting-bot
```

Install dependencies:

```
pip install flask
```

---

# Run the Web Chatbot

Start the Flask server:

```
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

You can now ask troubleshooting questions through the web interface.

Example:

```
disk full
pod restarting
service down
Help > to view what are the issues bot can help
```

---

# Run the CLI Bot

You can also run the chatbot directly in the terminal:

```
python bot.py
```

Example interaction:

```
You: disk full
Bot: Run 'df -h' to check disk usage and clear unnecessary files
```

Type:

```
help
```

to see all supported issues.

Type:

```
exit
```

to quit the program.

---

# Extending the Knowledge Base

To add new troubleshooting scenarios, edit:

```
knowledge.json
```

Example entry:

```
"memory high": "Use 'free -m'
```
