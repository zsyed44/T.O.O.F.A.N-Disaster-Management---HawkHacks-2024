import re

def initial_state():
    print("Hi there! I hope you're doing okay? I'm here to assist you in all the ways I can. So please tell me, how can I help you?")
    user_input = input("> ")
    return handle_input(user_input)

def handle_input(user_input):
    user_input = user_input.lower()

    if re.search(r'real person|human|911|emergency', user_input):
        return emergency_contact()
    elif re.search(r'lost|help', user_input):
        return lost_help()
    elif re.search(r'scared|afraid|fear', user_input):
        return scared_help()
    else:
        return default_response()

def emergency_contact():
    print("It seems like you need to talk to a real person. Please contact emergency services at 911.")
    return final_state()

def lost_help():
    print("I understand you're feeling lost and need help. Let's talk about it. How can I make you feel less anxious?")
    user_input = input("> ")
    print("Distress signal online. Rescue team on its way.")
    return final_state()

def scared_help():
    print("I understand you're feeling scared. Everything is going to be alright. Let's talk more about what's scaring you.")
    user_input = input("> ")
    print("It's okay to feel scared. You're not alone. We'll get through this together.")
    user_input = input("> ")
    print("Remember, you're safe and help is on the way if needed.")
    return final_state()

def default_response():
    print("Distress signal online. Rescue team on its way.")
    return final_state()

def final_state():
    print("Don't worry, everything will be fine. Someone will soon arrive and help you!")
    return None

def main():
    current_state = initial_state
    while current_state is not None:
        current_state = current_state()

if __name__ == "__main__":
    main()
