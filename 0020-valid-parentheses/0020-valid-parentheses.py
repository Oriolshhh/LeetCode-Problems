class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    
        for char in s:
            if char in ['(', '[', '{']: # opening bracket --> we add the bracket to the stack
                stack.append(char)
            else: # closing bracket
                if not stack: # if the stack is empty --> weve found a closing bracket with no opening brackets
                    return False
                
                # if is not empty check the validity of the last opening bracket with the closing bracket
                top = stack.pop()
                if (top == '(' and char != ')') or \
                   (top == '[' and char != ']') or \
                   (top == '{' and char != '}'):
                    return False

        return not stack