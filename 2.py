def check_parentheses(input_lines):
    outputs = []

    for line in input_lines:
        markers = [' '] * len(line)
        balance = 0

        for i, char in enumerate(line):
            if char == '(':
                balance += 1
            elif char == ')':
                if balance == 0:
                    markers[i] = '?'
                else:
                    balance -= 1

        balance = 0
        for i in range(len(line) - 1, -1, -1):
            char = line[i]
            if char == ')':
                balance += 1
            elif char == '(':
                if balance == 0:
                    markers[i] = 'x'
                else:
                    balance -= 1

        markers_string = ''.join(markers)
        outputs.append((line, markers_string))

    return outputs


input_lines = [
    "bge)))))))))",
    "((IIII)))))),",
    "()()()()(uuu",
    "))))UUUU((()"
]

outputs = check_parentheses(input_lines)

for line, markers in outputs:
    print(line)
    print(markers)