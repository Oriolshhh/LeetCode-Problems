class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numsMap = new HashMap<>();
        int[] result = new int[2];

        for(int i = 0; i < nums.length; i++) {
            if(!numsMap.isEmpty()) {
                if(numsMap.containsKey(target - nums[i])) {
                    result[0] = numsMap.get(target - nums[i]);
                    result[1] = i;

                    return result;
                }
            }

            numsMap.put(nums[i], i);
        }

        return result;
    }
}