# Week 9 – Chatbot Development

## Building an Interactive AI Chatbot using Ollama

### 1. Project Description
This project develops an interactive Education Chatbot using Python and Ollama. It uses the locally running Llama 3.2 large language model to answer user questions about education, programming, and technology.

### 2. Objectives
- Understand the architecture of an AI chatbot powered by a local LLM.
- Build a command-line chatbot using Python and Ollama.
- Maintain conversation history for context-aware responses.
- Save user questions and chatbot responses in CSV files.
- Analyze the strengths and limitations of chatbot responses.

### 3. Technologies Used
- Python
- Ollama
- Llama 3.2
- Pandas
- Jupyter Notebook
- Visual Studio Code

### 4. Project Structure
```text
Chatbot_Development/
├── dataset/
│   ├── chat_history.csv
│   ├── sample_questions.csv
│   ├── chatbot_logs.txt
│   └── responses.csv
├── notebook/
│   └── Week9_Chatbot_Development.ipynb
├── chatbot.py
├── README.md
└── requirements.txt
```

### 5. Installation
1. Install Python.
2. Install Ollama.
3. Download the Llama 3.2 model using:

   `ollama pull llama3.2`

4. Install the required Python libraries:

   `python -m pip install -r requirements.txt`

### 6. How to Run
1. Open the project folder in Visual Studio Code.
2. Open the terminal in the project directory.
3. Run the chatbot:

   `python chatbot.py`

4. Enter a question when the `You:` prompt appears.
5. Type `exit` to end the conversation.

### 7. Output Files
- `chat_history.csv` stores timestamps, session IDs, user questions, and chatbot responses.
- `responses.csv` stores user questions and generated responses.
- `chatbot_logs.txt` stores readable conversation logs.
- `sample_questions.csv` contains 20 sample education questions.

### 8. Conclusion
The project demonstrates how to build an interactive chatbot using a locally running large language model. It maintains conversation context within a session and records user interactions for further analysis. The project provides a foundation for future integration with LangChain.
