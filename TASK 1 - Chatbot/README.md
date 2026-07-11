# Task 1 - Rule-Based Chatbot

## CodSoft Internship

A simple chatbot built in Python that responds to user inputs based on
predefined rules. It uses **regex pattern matching** combined with
**if-else logic** to detect user intent and reply appropriately.

## Features
- Greeting, farewell, and small-talk responses
- Tells current time and date
- Randomized responses for a more natural feel
- Fallback responses for unrecognized input

## How to Run
```bash
python chatbot.py
```

Then chat with the bot in your terminal. Type `bye`, `exit`, or `quit` to end
the conversation.

## Example
```
CodBot: Hi! I'm a rule-based chatbot. Type 'bye' to exit.
You: hello
CodBot: Hey! What's up?
You: what time is it
CodBot: The current time is 14:32:10.
You: bye
CodBot: Goodbye! Have a great day!
```

## Concepts Used
- Regular expressions (`re` module) for pattern matching
- If-else / conditional rule matching
- Basic conversation loop design

## Author
Built as part of the CodSoft Internship program.
