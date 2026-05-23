from flask import Flask, request, jsonify, render_template #import flask tools
from anthropic import Anthropic #import claude AI
from dotenv import load_dotenv #import tool to read .env file
import os #lets python talk to the operating system
from database import init_db, save_message, load_messages # import database functions

load_dotenv() #() means load_dotenv is running 
app = Flask(__name__) #flask server created and saved as app
client = Anthropic() #whenever we want to talk to Claude AI we use client as the variable

init_db() # set up the database when server starts
conversation_history = load_messages() # load previous messages from database

# when someone visits the homepage, show them the chatbot webpage
@app.route("/")
def home():
    return render_template("index.html") 

#receiving messages from webpage
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message") # grab the message from the webpage and save it
    conversation_history.append({
        "role": "user",
        "content": user_message
    }) # every message sent from user is labelled
    save_message('user', user_message) # save user message to database
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024, #word limit, stops claude from sending paragraphs
        system="You are a friendly holiday planning assistant. Help users plan their perfect holiday by asking about their budget, preferences, travel dates, and destination wishes. Give specific recommendations and tips.",
        messages=conversation_history
    )
    assistant_message = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    }) # just like user, we have to save claudes response to history
    save_message('assistant', assistant_message) # save claude's response to database
    return jsonify({"response": assistant_message}) #sends back the response to webpage

#checks if file is being run directly, also shows error message if something is wrong
if __name__ == "__main__":
    app.run(debug=True)