class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def evaluate_expression(expression):
    stack = Stack()
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token == '(':
            stack.push(token)
        elif token == ')':
            sub_expr = []
            while stack.peek() != '(':
                sub_expr.append(stack.pop())
            stack.pop()  # Remove the '(' from the stack

            result = evaluate_subexpression(sub_expr)
            stack.push(result)
        else:
            stack.push(token)

    result = evaluate_subexpression(stack.items)
    return result

def evaluate_subexpression(sub_expr):
    stack = Stack()
    for token in sub_expr:
        if isinstance(token, (int, float)):
            stack.push(token)
        elif token.replace('.', '', 1).isdigit() or (token[0] == '-' and token[1:].replace('.', '', 1).isdigit()):
            stack.push(float(token))
        elif token in ('+', '-', '*', '/'):
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.push(result)

    return stack.pop()



def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero")
        return operand1 / operand2

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python ex1.py 'expression'")
        sys.exit(1)

    expression = sys.argv[1]
    result = evaluate_expression(expression)
    print(result)
