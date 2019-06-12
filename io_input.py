def reserve(text):
    return text[::-1]


def is_palindrome(text):
    return text == reserve(text)


Running = True
while Running:
    something = input("Enter text:")
    if is_palindrome(something):
        print("Yes,it is palindrome")
        Running = False
    else:
        print("No,it is not a palindrome")
