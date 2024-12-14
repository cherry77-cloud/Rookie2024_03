def evaluate_expression(expression: str) -> int:
    num_stack = []
    op_stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def eval_top():
        b = num_stack.pop()
        a = num_stack.pop()
        op = op_stack.pop()
        if op == '+':
            num_stack.append(a + b)
        elif op == '-':
            num_stack.append(a - b)
        elif op == '*':
            num_stack.append(a * b)
        elif op == '/':
            if a * b < 0 and a % b != 0:
                num_stack.append(a // b + 1)
            else:
                num_stack.append(a // b)

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            x = 0
            while i < len(expression) and expression[i].isdigit():
                x = x * 10 + int(expression[i])
                i += 1
            num_stack.append(x)
            i -= 1
        elif expression[i] == '(':
            op_stack.append(expression[i])
        elif expression[i] == ')':
            while op_stack[-1] != '(':
                eval_top()
            op_stack.pop()
        else:
            while op_stack and op_stack[-1] != '(' and precedence[op_stack[-1]] >= precedence[expression[i]]:
                eval_top()
            op_stack.append(expression[i])
        i += 1

    while op_stack:
        eval_top()

    return num_stack.pop() if num_stack else 0


if __name__ == "__main__":
    expression = input().strip()
    print(evaluate_expression(expression))
