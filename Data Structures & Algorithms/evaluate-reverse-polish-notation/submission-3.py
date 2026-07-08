class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        operands = []
        
        for token in tokens:
            if token in operators:
                b = operands.pop()
                a = operands.pop()

                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b                 
                elif token == '*': 
                    res = a * b
                elif token == '/':
                    res = int(a / b)
                # print('a,b', a,b, 'res=', res)
                operands.append(res)
                # print(operands)
            else:
                operands.append(int(token))
        
        return operands[0]