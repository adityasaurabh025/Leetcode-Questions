class Solution {
    
    //According to me this is my time complextity, not sure about TC.
    //Time Complextiy -> O(n) for first Iteration + O(n) for one more iteration + O(k) approx for last one
    // Space Complextity --> O(N)+ O(N) overall O(N).
    
    public List<String> topKFrequent(String[] words, int k) {
        // make the list to store the output res.
        List<String> res = new ArrayList<>();
        
        // Make a treemap , so that it store strings in sorted order
        // it will help in when there repetitions is same.
        TreeMap<String,Integer> tmap = new TreeMap<>();
        // fill our tmap .
        for(String s : words)
            tmap.put(s,tmap.getOrDefault(s,0) + 1);
        
        // Make another Treemap to store values according to their repetition 
        // and store them according to Integer values in reverse order !
        TreeMap<Integer,String> treemap = new TreeMap<>(Collections.reverseOrder());
        
        for(Map.Entry m : tmap.entrySet()){
            // If key value is not present put it normally.
            if(treemap.get(m.getValue()) == null)
                treemap.put((Integer)m.getValue(),(String)m.getKey());
            else{
                // if it is present already then we just concatnate it with previously
                // present string which is already in sorted order.
                String val = treemap.get(m.getValue());
                treemap.put((Integer)m.getValue(),val + " " + (String)m.getKey());
            }
        }
        
        
        for(Map.Entry m : treemap.entrySet()){
            if(k>0){
                // Iterate through the map 
                // Take the values and split it against backspace
                String str = (String)m.getValue();
                String[] arr = str.split(" ");
                // Just put it in our res and reduce value of k until it becomes zero.
                for(int i = 0; i<arr.length; i++){
                    if(k>0){
                         res.add(arr[i]);
                         k--;
                    }
                }
            }
        }

        return res;
        
    }
}






//Approach-2 --HashMap
// class Solution {
//   public static List<String> topKFrequent(String[] words, int k) {
//         List<String> ans = new ArrayList<>();
//         Map<String, Integer> freqMap = new HashMap<>();
//         for (String word : words) {
//             freqMap.put(word, freqMap.getOrDefault(word, 0) + 1);
//         }

//         ans.addAll(freqMap.keySet());

//         Collections.sort(ans, (o1, o2) -> {
//             if (freqMap.get(o1) == freqMap.get(o2)) {
//                 return o1.compareTo(o2);
//             }

//             return freqMap.get(o2) - freqMap.get(o1);
//         });

//         return ans.subList(0, k);
//     }
// }