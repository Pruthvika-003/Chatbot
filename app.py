from flask import Flask, render_template, request

app = Flask(__name__)

class SimpleChatbot:
    def __init__(self):
        self.name = "Chatbot"
        self.messages = []

    def greet_user(self):
        return f"{self.name}: Hello! How can I help you today?"

    def provide_general_info(self):
        return f"{self.name}: I am a simple chatbot designed to handle simple questions asked by the users."

    def respond_to_faq(self, question):
        faqs = {
            "reset password": "To reset your password, please visit our website and use the 'Forgot Password' feature.",
            "working hours": "I am available 24/7 to assist you!",
        }
        response = faqs.get(question.lower(), f"I'm sorry, I don't have information about that.")
        return f"{self.name}: {response}"

chatbot = SimpleChatbot()

@app.route('/')
def index():
    return render_template('index.html', messages=chatbot.messages)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    if user_input.lower() == 'exit':
        chatbot.messages.append({"user_input": user_input, "bot_response": f"{chatbot.name}: Goodbye! Have a great day!"})
        return render_template('index.html', messages=chatbot.messages)

    if any(greeting in user_input.lower() for greeting in ["hello", "hi", "hey"]):
        response = chatbot.greet_user()
    elif "what can you do" in user_input.lower() or "tell me about yourself" in user_input.lower():
        response = chatbot.provide_general_info()
    elif "?" in user_input:
        response = chatbot.respond_to_faq(user_input)
    else:
        response = f"{chatbot.name}: I'm not sure how to respond to that. Ask me something else."

    chatbot.messages.append({"user_input": user_input, "bot_response": response})

    return render_template('index.html', messages=chatbot.messages)

if __name__ == "__main__":
    app.run(debug=True)
