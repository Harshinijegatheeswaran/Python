def precedence(operator):
    if operator == '^':
        return 3
    elif operator in ('*', '/'):
        return 2
    elif operator in ('+', '-'):
        return 1
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for char in expression:
       
        if char.isalnum():
            postfix += char

       
        elif char == '(':
            stack.append(char)

       
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(char)):
                postfix += stack.pop()

            stack.append(char)

   
    while stack:
        postfix += stack.pop()

    return postfix

expression = input("Enter an infix expression: ")

result = infix_to_postfix(expression)

print("Postfix expression:", result)
