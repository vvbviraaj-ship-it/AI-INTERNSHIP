questions_answers = {
    'hi': 'Hello! How can I help you?',
    'hello': 'Hey there! Nice to meet you.',
    'how are you': 'I am fine, thanks for asking!',
    'what is your name': 'I am a simple chatbot.',
    'what can you do': 'I can answer basic questions. Try asking me something!',
    'bye': 'Goodbye! Have a great day!',
    'thanks': 'You\'re welcome!',
    'help': 'Try asking: hi, how are you, what is your name, bye'
}

EXIT_KEYWORDS = {'bye', 'exit', 'quit'}

print("Chatbot is ready! Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    if not user:
        continue

    if user in EXIT_KEYWORDS:
        print("Bot:", questions_answers.get(user, "Goodbye!"))
        break

    if user in questions_answers:
        print("Bot:", questions_answers[user])

    else:
        matched = False
        for key in questions_answers:
            if key in user:
                print("Bot:", questions_answers[key])
                matched = True
                break

        if not matched:
            print("Bot: Sorry, I don't understand. Type 'help' to see what I can do.")