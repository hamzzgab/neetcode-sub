class Solution {
    public int[] topKFrequent(int[] nums, int k) {        
        List<Integer>[] freq = new List[nums.length + 1];
        Map<Integer, Integer> hash = new HashMap<>();

        for (int i=0; i<freq.length; i++){
            freq[i] = new ArrayList<>();
        }

        for (int n: nums){
            hash.put(n, hash.getOrDefault(n, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry: hash.entrySet()){
            freq[entry.getValue()].add(entry.getKey());            
        }

        int[] res = new int[k];
        int index = 0;
        for (int i = freq.length - 1; i>0; i --){
            for (int n: freq[i]){
                res[index++] = n;
                if (index == k){
                    return res;
                }
            }
        }
        return res;
    }
}
