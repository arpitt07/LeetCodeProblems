class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }

        pos = 0

        while len(tokens) > 1:
            while tokens[pos] not in '+-*/':
                pos += 1

            curr = tokens[pos]
            val1 = int(tokens[pos - 2])
            val2 = int(tokens[pos - 1])

            operate = operations[curr]
            tokens[pos] = operate(val1, val2)

            tokens.pop(pos - 2)
            tokens.pop(pos - 2)

            pos -= 1

        return tokens[0]