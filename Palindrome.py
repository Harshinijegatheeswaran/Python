from collections import deque

def check_palindrome():
    user_input = input("Enter a string: ")
    stack = []
    queue = deque()
    cleaned_chars = []
   
    for char in user_input:
        if char.isalnum():  
            clean_char = char.lower()
            stack.append(clean_char)
            queue.append(clean_char)
            cleaned_chars.append(clean_char)
           
    cleaned_string = "".join(cleaned_chars)
    print(cleaned_string)
   
    is_palindrome = True
    while stack:
        if stack.pop() != queue.popleft():
            is_palindrome = False
            break
           
    if is_palindrome:
        print("IS a palindrome.")
    else:
        print("is NOT a palindrome.")

if __name__ == "__main__":
    check_palindrome()
