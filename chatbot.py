
import csv
import uuid
from datetime import datetime
from pathlib import Path

import ollama

# Project settings
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"

MODEL = "llama3.2"
DOMAIN = "Education"

CHAT_HISTORY_FILE = DATASET_DIR / "chat_history.csv"
RESPONSES_FILE = DATASET_DIR / "responses.csv"
LOG_FILE = DATASET_DIR / "chatbot_logs.txt"

SYSTEM_PROMPT = """
You are a helpful Education Chatbot.
Answer questions about education, programming, and technology
in simple English.
Give clear explanations and examples when useful.
If you are unsure about an answer, say so.
Do not invent facts. For important or complex topics,
encourage the user to verify information with reliable sources.
"""

# Create the dataset folder if necessary
DATASET_DIR.mkdir(parents=True, exist_ok=True)

# Create CSV files with column headings
def prepare_csv(file_path, headers):
    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)


prepare_csv(
    CHAT_HISTORY_FILE,
    ["timestamp", "session_id", "user_question", "chatbot_response"]
)

prepare_csv(
    RESPONSES_FILE,
    ["timestamp", "question", "response"]
)


def save_csv(file_path, row):
    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(row)


def save_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(message + "\n")


def main():
    session_id = str(uuid.uuid4())[:8]

    # Conversation history keeps previous messages for context.
    conversation = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    print("=" * 55)
    print("       EDUCATION CHATBOT USING OLLAMA")
    print("=" * 55)
    print(f"Model: {MODEL}")
    print(f"Domain: {DOMAIN}")
    print("Ask questions about education, programming, or technology.")
    print("Type 'exit' to stop the chatbot.")
    print("-" * 55)

    save_log(
        f"\nSession started: {datetime.now().isoformat(timespec='seconds')} "
        f"| Session ID: {session_id}"
    )

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                print("Please enter a question.")
                continue

            if user_input.lower() == "exit":
                print("Chatbot: Goodbye! Keep learning.")
                break

            # Add the user's question to the conversation.
            conversation.append(
                {"role": "user", "content": user_input}
            )

            # Send the full conversation to the local LLM.
            result = ollama.chat(
                model=MODEL,
                messages=conversation
            )

            answer = result["message"]["content"].strip()

            print(f"\nChatbot: {answer}")

            # Add the assistant's answer to conversation history.
            conversation.append(
                {"role": "assistant", "content": answer}
            )

            timestamp = datetime.now().isoformat(timespec="seconds")

            # Save the conversation to chat_history.csv.
            save_csv(
                CHAT_HISTORY_FILE,
                [timestamp, session_id, user_input, answer]
            )

            # Also save question-answer pairs to responses.csv.
            save_csv(
                RESPONSES_FILE,
                [timestamp, user_input, answer]
            )

            # Save a readable log in chatbot_logs.txt.
            save_log(f"\nTimestamp: {timestamp}")
            save_log(f"Session ID: {session_id}")
            save_log(f"User: {user_input}")
            save_log(f"Chatbot: {answer}")

        except KeyboardInterrupt:
            print("\nChatbot stopped by the user.")
            break

        except Exception as error:
            print(f"\nAn error occurred: {error}")
            print("Check that Ollama is running and the model is available.")
            save_log(f"Error at {datetime.now().isoformat()}: {error}")

    save_log(
        f"Session ended: {datetime.now().isoformat(timespec='seconds')} "
        f"| Session ID: {session_id}"
    )
    print("\nConversation files are saved in the dataset folder.")


if __name__ == "__main__":
    main()
