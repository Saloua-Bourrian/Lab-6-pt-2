def encode(password):
    result = ''
    for num in password:
        new_num = str((int(num) + 3) % 10)
        result += new_num

    return result


def decode(password):
    result = ''
    for num in password:
        new_num = str((int(num) - 3) % 10)
        result += new_num

    return result


def menu():
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def main():

    while True:
        menu()
        option = input(f"Please enter an option: ")

        if option == '1':
            password = input(f"Please enter your password to encode: ")
            password2 = encode(password)
            print('Your password has been encoded and stored!')

        elif option == '2':
            decode_num = decode(password2)
            print(f"The encoded password is {password2}, and the original password is {decode_num}.")

        elif option == '3':
            break

        else:
            print("Invalid Choice")




if __name__ == '__main__':
    main()
