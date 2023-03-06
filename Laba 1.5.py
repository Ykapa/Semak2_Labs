check = True
S = ""

while check == True:
    word = input("Введите слово: ").replace(' ', '')
    if word == "stop" or word == "стоп":
        check = False
        print(S)
    else:
        S = S + word + " "