import urwid


def is_very_long(password):
    return len(password) >= 12


def has_str(password):
    return any(letter.isalpha() for letter in password)


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isalnum() for letter in password)


def resultat(password):
    checks = [
        is_very_long,
        has_str, 
        has_digit,
        has_upper_letters, 
        has_lower_letters,
        has_symbols
    ]
    return sum(2 for check in checks if check(password))


def on_ask_change(edit, new_edit_text):
    score = resultat(new_edit_text)
    reply.set_text(f"Рейтинг вашего пароля: {score}")


def main():
    global reply
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("Рейтинг вашего пароля: 0")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == "__main__":
    main()
