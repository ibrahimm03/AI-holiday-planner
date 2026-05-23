# AI Holiday Planner 🌍

An AI-powered holiday planning chatbot built with Python, Flask, and Claude AI. Users can get personalised holiday recommendations for destinations, budgets, and hotels through a beautiful conversational interface.

## Features

- Beautiful homepage with animated UI
- AI chatbot powered by Claude (Anthropic)
- Conversation history saved to a database
- Quick start cards for Destinations, Budgets, and Hotels
- Fully responsive design

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **AI:** Anthropic Claude API
- **Database:** SQLite

## Project Structure

```
ai-holiday-planner/
├── app.py              # Flask backend server
├── database.py         # Database setup and functions
├── .env                # API key (not uploaded)
├── .gitignore          # Protects sensitive files
└── templates/
    └── index.html      # Frontend webpage
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/ibrahimm03/AI-holiday-planner.git
cd AI-holiday-planner
```

### 2. Install dependencies
```bash
pip3 install flask anthropic python-dotenv
```

### 3. Add your API key
Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=your-api-key-here
```
Get your API key from [console.anthropic.com](https://console.anthropic.com)

### 4. Run the app
```bash
python3 app.py
```

### 5. Open in browser
```
http://127.0.0.1:5000
```

## How It Works

1. User visits the homepage and clicks a card or the start button
2. JavaScript sends the message to the Flask server
3. Flask sends the conversation history to Claude AI
4. Claude responds with personalised holiday advice
5. The response is saved to the SQLite database and displayed in the chat window

## Author

Ibrahim — [github.com/ibrahimm03](https://github.com/ibrahimm03)
