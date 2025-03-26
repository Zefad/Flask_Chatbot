# Flask Chatbot

## Overview  
A simple chatbot application built with Flask and SpaCy. The chatbot uses natural language processing to match user inputs to a predefined set of FAQs and provides responses based on similarity scores.

## Features  
- Natural language processing using SpaCy's similarity function
- Predefined set of FAQs for responses
- User-friendly web interface with chat functionality
- Basic conversation handling
- Session-based conversation history, cleared when the user leaves the page

## Technologies Used  
**Flask:** Web framework for Python.

**SpaCy:** Library for natural language processing.

**HTML:** Structure of the web interface.

**CSS:** Styling for the chat interface.

**JavaScript:** Client-side interactivity. 

## Installation  

### Clone the Repository  
```bash
git clone https://github.com/Zefad/Flask_Chatbot.git  
cd Flask_Chatbot
```
## Install Dependecies:
```
pip install -r requirements.txt
python -m spacy download en_core_web_md
```
## Run Flask Server:
```
python app.py
```
## Open in Browser:
```
http://127.0.0.1:5000
```
