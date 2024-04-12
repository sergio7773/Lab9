def encoder(password):
    encoded_password = ""
    for digit in password:
        digit = int(digit)
        digit += 3
        encoded_password += str(digit)
    return encoded_password

def decoder(encoded_password):
    emptystring = ""
    for i in encoded_password:
        i = int(i)
        if i == 2:
            emptystring = emptystring + str(9)
        elif i == 1:
            emptystring = emptystring + str(8)
        elif i == 0:
            emptystring = emptystring + str(7)
        else:
            i -= 3
            emptystring = emptystring + str(i)
    return emptystring


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
            decoded_password = decoder(encoded_password)
            print(decoded_password)
            print(f"The encoded password is {encoded_password},"
                  f" and the original password is {decoded_password}.\n")
        elif option == 3:
            encoder_on = False


if __name__ == "__main__":
    main()
