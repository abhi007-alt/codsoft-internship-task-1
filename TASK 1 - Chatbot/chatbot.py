"""
Rule-Based Chatbot
CodSoft Internship - Task 1

A simple chatbot that responds to user inputs using predefined rules
and pattern matching (if-else + regex).
"""

import re
import random
from datetime import datetime


class RuleBasedChatbot:
    def __init__(self, name="Bot"):
        self.name = name
        # Each rule: (list of regex patterns, list of possible responses)
        self.rules = [
            (r'\b(hi|hello|hey|hola)\b',
             ["Hello there! How can I help you today?",
              "Hey! What's up?",
              "Hi! Nice to see you."]),

            (r'\b(bye|goodbye|see you|exit|quit)\b',
             ["Goodbye! Have a great day!",
              "See you later!",
              "Bye! Take care."]),

            (r'\b(how are you|how\'s it going)\b',
             ["I'm just a bunch of code, but I'm doing great! How about you?",
              "Doing well, thanks for asking!"]),

            (r'\b(your name|who are you)\b',
             [f"I'm {self.name}, your friendly rule-based chatbot.",
              f"You can call me {self.name}."]),

            (r'\b(time)\b',
             [lambda: f"The current time is {datetime.now().strftime('%H:%M:%S')}."]),

            (r'\b(date|today)\b',
             [lambda: f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."]),

            (r'\b(thanks|thank you)\b',
             ["You're welcome!", "No problem at all!", "Anytime!"]),

            (r'\b(your age|how old are you)\b',
             ["I don't age, I just keep running on rules!"]),

            (r'\b(help|what can you do)\b',
             ["I can chat about greetings, time, date, and basic small talk. "
              "Try asking me 'what time is it' or just say hello!"]),

            (r'\b(weather)\b',
             ["I can't check live weather yet, but I hope it's sunny where you are!"]),
        ]

        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting... tell me more.",
            "Hmm, I don't have a rule for that yet.",
            "Sorry, I didn't quite get that.",
        ]

    def get_response(self, user_input: str) -> str:
        text = user_input.lower().strip()

        for patterns, responses in self.rules:
            if re.search(patterns, text):
                choice = random.choice(responses)
                # allow lazy-evaluated responses like time/date
                return choice() if callable(choice) else choice

        return random.choice(self.default_responses)

    def chat(self):
        print(f"{self.name}: Hi! I'm a rule-based chatbot. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if not user_input.strip():
                continue

            response = self.get_response(user_input)
            print(f"{self.name}: {response}")

            if re.search(r'\b(bye|goodbye|exit|quit)\b', user_input.lower()):
                break


if __name__ == "__main__":
    bot = RuleBasedChatbot(name="CodBot")
    bot.chat()
