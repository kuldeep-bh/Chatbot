# Camping Chatbot

Welcome to the Camping Chatbot — a simple rule-based chatbot built using Python's NLTK library and deployed with Streamlit. This chatbot is designed to answer questions about camping, outdoor activities, and basic general conversation.

# Features

Rule-based natural language processing using nltk.chat.util.Chat

Friendly camping-related tips and tricks

Simple and responsive UI using Streamlit

Maintains chat history during a session

Easy-to-extend response patterns

# Technologies Used

Python 3

NLTK (Natural Language Toolkit)

Streamlit

# Installation

Clone the repository:

git clone https://github.com/your-username/camping-chatbot.git
cd camping-chatbot


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


If requirements.txt doesn’t exist, manually install:

pip install streamlit nltk

#Running the Chatbot

Launch the chatbot with Streamlit:

streamlit run app.py


Then open the provided local URL (usually http://localhost:8501) in your browser.

# Project Structure
camping-chatbot/
│
├── app.py               # Main Streamlit app
├── README.md            # Project readme (this file)
└── requirements.txt     # Python dependencies (optional)

# Example Inputs

Try asking things like:

"What should I pack for camping?"

"How to stay warm while camping?"

"Is it safe to camp alone?"

"How to cook while camping?"

"Hi"

"How are you?"

Type quit to end the chat session.

# Customize It!

You can add more conversation patterns by editing the pairs list in app.py. Each pattern is a list containing:

[
    r"(.*)your question regex(.*)",
    ["Response 1", "Response 2", ...]
]


To make it more intelligent, consider integrating machine learning or using a pre-trained chatbot framework.

#  Author

Developed by Kuldeep Singh

"Make every adventure count!"
