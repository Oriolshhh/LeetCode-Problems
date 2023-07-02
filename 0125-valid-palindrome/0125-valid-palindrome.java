class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            if (isAlphanumeric(s.charAt(l)) && isAlphanumeric(s.charAt(r))) {
                if (Character.toLowerCase(s.charAt(l)) 
                    != Character.toLowerCase(s.charAt(r))) {
                    return false;
                }
                l++; r--;
            } else {
                if (!isAlphanumeric(s.charAt(l))) {
                    l++;
                }
                if (!isAlphanumeric(s.charAt(r))) {
                    r--;
                }
            }
        }

        return true;
    }

    private boolean isAlphanumeric(char c) {
        return Character.isLetterOrDigit(c);
    }

}