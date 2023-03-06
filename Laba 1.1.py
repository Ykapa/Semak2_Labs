pass1 = input("Введите пароль: ").replace(' ', '')
pass2 = input("Повторите пароль: ").replace(' ', '')

if pass1 == pass2:
    print("Пароль принят!")
else:
    print("Пароль не принят!")
