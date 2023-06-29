class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        HashMap <Character, Integer> sMap = new HashMap<>();
        HashMap <Character, Integer> tMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if(sMap.get(s.charAt(i)) == null) sMap.put(s.charAt(i), 1);
            else sMap.put(s.charAt(i), sMap.get(s.charAt(i)) + 1);
            
            if(tMap.get(t.charAt(i)) == null) tMap.put(t.charAt(i), 1);
            else tMap.put(t.charAt(i), tMap.get(t.charAt(i)) + 1);
        }


        for (char c : sMap.keySet()) {
            if(tMap.get(c) == null) return false; 
            if(!tMap.get(c).equals(sMap.get(c))) return false; 
        } 
        
        return true; 
                
    }
}