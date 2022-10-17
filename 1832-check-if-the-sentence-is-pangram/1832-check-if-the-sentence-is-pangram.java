class Solution {
    public boolean checkIfPangram(String sentence) {
        // Create a hashSet containing only unique values...
        Set<Character> hset = new HashSet<>();
        // Add all elements to hset...
        for (final char ch : sentence.toCharArray())
            hset.add(ch);
        // Check the size of the hset if it is 26 then the string is a pangram...
        return hset.size() == 26;
    }
}



//Approach-2

// int[] arr = new int[26];

//     for(int i=0;i<sentence.length();i++)
//        arr[sentence.charAt(i)-'a']+=1;

//     for(int i=0;i<26;i++){
//        if(arr[i] == 0)
//         return false;
//     }
//     return true;
// }