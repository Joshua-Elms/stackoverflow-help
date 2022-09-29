def main():
    text_to_encrypt = input("enter text to encrypt: ")
    print()
    shift_amount = int(input("enter shift amount: "))

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    shifted = ""

    for ch in text_to_encrypt:
        if ch == " ":
            shifted += ch
            continue
        num = ord(ch) - 97
        shifted += alphabet[num + shift_amount % len(alphabet)]

    print(shifted)

main()