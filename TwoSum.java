class Solution {
    public int[] twoSum(int[] nums, int target) {
        // the approach using hashtable
        int[] result=new int[2];
        HashMap<Integer,Integer> ht=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(ht.containsKey(target-nums[i])){
                result[0]=i;
                result[1]=ht.get(target-nums[i]);
                return result;
            }
            ht.put(nums[i],i);
        }
        return result;
        // tc = O(N)
        // sc=O(N)
    }
}
