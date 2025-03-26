from flask import Flask, request, render_template, session, redirect, url_for
import os
import spacy

app = Flask(__name__)
app.secret_key = os.urandom(24)

nlp = spacy.load("en_core_web_md")

faq_data = [
    {
        "question": "hello",
        "response": "Hello! How can I assist you today?",
        "doc": nlp("hello")
    },
    {
        "question": "what is your name?",
        "response": "I am ChatBot, your friendly assistant.",
        "doc": nlp("what is your name?")
    },
    {
        "question": "how are you?",
        "response": "I'm good, thanks for asking!",
        "doc": nlp("how are you?")
    },
    {
        "question": "what can you do?",
        "response": "I can answer your FAQs and help with basic tasks.",
        "doc": nlp("what can you do?")
    },
    {
        "question": "what is the weather?",
        "response": "I'm not able to check the weather, but I hope it's nice outside!",
        "doc": nlp("what is the weather?")
    },
    {
        "question": "how old are you?",
        "response": "I am a bot, so I don't really age.",
        "doc": nlp("how old are you?")
    },
    {
        "question": "tell me a joke",
        "response": "Why did the chicken cross the road? To get to the other side!",
        "doc": nlp("tell me a joke")
    },
    {
        "question": "how do i reset my password?",
        "response": "Please visit our password reset page and follow the instructions.",
        "doc": nlp("how do i reset my password?")
    },
    {
        "question": "what time is it?",
        "response": "I don't have a clock, but you can check your device for the current time.",
        "doc": nlp("what time is it?")
    },
    {
        "question": "where are you located?",
        "response": "I exist in the cloud, so I don't have a physical location.",
        "doc": nlp("where are you located?")
    },
    {
        "question": "what is your purpose?",
        "response": "I'm here to assist you with any questions you might have.",
        "doc": nlp("what is your purpose?")
    }
]

def get_response(user_input):
    doc_input = nlp(user_input)
    best_match = None
    highest_similarity = 0.0

    for faq in faq_data:
        similarity = doc_input.similarity(faq["doc"])
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = faq

    if best_match and highest_similarity > 0.5:
        return best_match["response"]
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize conversation if not already in session.
    if "conversation" not in session:
        session["conversation"] = []
    conversation = session["conversation"]

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        conversation.append({"sender": "user", "text": user_input})
        response = get_response(user_input)
        conversation.append({"sender": "bot", "text": response})
        session["conversation"] = conversation  # update session
        return redirect(url_for("index"))

    return render_template("index.html", conversation=conversation)

# New endpoint to clear the conversation.
@app.route("/clear", methods=["POST"])
def clear():
    session.pop("conversation", None)
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)