class Solution {
     public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> output = new ArrayList<>();
        HashMap<String, List<String>> map = new HashMap<>();

        for(String str : strs) {
            //Sort the string to get the same index in the map for all anagrams
            char[] letters = str.toCharArray();
            Arrays.sort(letters);
            String key = new String(letters);

            if(map.containsKey(key)) { //If the map already contains the anagram of the string
                List<String> aux = map.get(key);
                aux.add(str);
                map.put(key, aux);
            } else { //If not, we add the string to the map
                List<String> aux = new ArrayList<>();
                aux.add(str);
                map.put(key, aux);
            }
        }

        output.addAll(map.values());
        return output;
    }
}