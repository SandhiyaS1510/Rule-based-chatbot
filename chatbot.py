import re
import random
import datetime

def get_response(user_input):
    user_input = user_input.lower()

    # Greeting responses
    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    greeting_responses = ["Hello! How can I help?", "Hey there!", "Hi! What do you need help with?"]

    # Check for greeting
    if any(word in user_input for word in greetings):
        return random.choice(greeting_responses)

    # How are you responses
    if re.search(r"\bhow are you\b", user_input):
        return "I'm just a bot, but I'm doing great! What about you?"

    # Name query
    if re.search(r"\b(your name|who are you)\b", user_input):
        return "I'm a simple rule-based chatbot, here to assist you!"

    # Time query
    if re.search(r"\btime\b", user_input):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # Date query
    if re.search(r"\bdate\b", user_input):
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today's date is {current_date}."

    # Weather query (simple response)
    if re.search(r"\b(weather|temperature)\b", user_input):
        return "I can't check the weather yet, but you can visit a weather website!"

    # Jokes
    if re.search(r"\bjoke\b", user_input):
        jokes = [
            "Why did the computer catch a cold? Because it left its Windows open!",
            "Why don’t programmers like nature? It has too many bugs.",
            "Why do Java developers wear glasses? Because they don’t see sharp!"
        ]
        return random.choice(jokes)

    # Fun facts
    if re.search(r"\bfact\b", user_input):
        facts = [
            "Did you know? Honey never spoils!",
            "Fun fact: The Eiffel Tower can be 15 cm taller during the summer.",
            "Interesting fact: A group of flamingos is called a 'flamboyance'!"
        ]
        return random.choice(facts)

    # Goodbye messages
    if re.search(r"\b(bye|goodbye|see you)\b", user_input):
        return "Goodbye! Have a great day!"

    # Default response
    return "I'm not sure how to respond to that. Can you rephrase?"

# Main chatbot function
def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
