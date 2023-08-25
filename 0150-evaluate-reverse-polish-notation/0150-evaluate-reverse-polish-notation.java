class Solution {
    public int evalRPN(String[] tokens) {
         Stack<Integer> stack = new Stack<>();
        
        for (String token : tokens) {
            if (token.matches("-?\\d+")) stack.push(Integer.parseInt(token));
            else {
                int num2 = stack.pop();
                int num1 = stack.pop();
                if (token.equals("+")) {
                    stack.push(num1 + num2);
                } else if (token.equals("-")) {
                    stack.push(num1 - num2);
                } else if (token.equals("*")) {
                    stack.push(num1 * num2);
                } else if (token.equals("/")) {
                    stack.push(num1 / num2);
                }
            }
        }
        
        return stack.peek();
    }

}