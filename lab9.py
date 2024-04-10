def encoder(password):
    encoded_password = ""
    for digit in password:
        digit = int(digit)
        digit += 3
        encoded_password += str(digit)
    return encoded_password


def main():
    encoder_on = True
    while encoder_on:
        print("Menu\n-------------")
        print(
            "1. Encode\n"
            "2. Decode\n"
            "3. Quit\n"
        )
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {encoded_password},"
                  f" and the original password is {password}.\n")
        elif option == 3:
            encoder_on = False


if __name__ == "__main__":
    main()
