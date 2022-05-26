def check_palindrome(text):
    text = text.replace(' ','')
    text = text.lower()
    text = text.replace(',','')
    if text == text[::-1]:
        print(True)
    else:
        print(False)
check_palindrome('Кит на море, не романтик')
