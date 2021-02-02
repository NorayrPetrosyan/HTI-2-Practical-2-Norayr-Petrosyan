def is_palindrome(text,i=0):
    half = len(text)//2

    if i == half:
        return 'Yes'

    if text[i] == text[-1-i]:
        return is_palindrome(text,i+1)

    return 'No'

text = input("Enter a text: ")
print(is_palindrome(text))