def ask_user():
    return input('Ask me anything: ')
    


def get_answer ():
    while True:
        user_say = ask_user()
        if user_say == 'пока':
            break

get_answer()