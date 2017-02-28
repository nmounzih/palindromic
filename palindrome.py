import re


def is_palindrome(sentence):
    sentence = re.sub(r'[^A-Za-z]', "", sentence.lower())
    if sentence == "":
        return True
    if sentence[0] == sentence[-1]:
        new_sentence = sentence[1: -1]
        return is_palindrome(new_sentence)
    return False


def main():
    user_input = input("Is it a palindrome? ")
    print(is_palindrome(user_input))
    if is_palindrome(user_input) is True:
        print("Yes, it is a palindrome.")
    else:
        print("No, it is not a palindrome.")


if __name__ == '__main__':
    main()
