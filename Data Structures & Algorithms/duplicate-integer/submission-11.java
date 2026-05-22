class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> duplicateNums = new HashSet<Integer>();

        for (int num: nums){
            if (duplicateNums.contains(num)){
                return true;
            }
            duplicateNums.add(num);
        }

        return false;
    }
}