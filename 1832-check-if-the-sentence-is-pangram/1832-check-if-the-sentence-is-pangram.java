class Solution {
    public boolean checkIfPangram(String sentence) {
        Set<Character> hset= new HashSet<>();
        
        for(char ch: sentence.toCharArray())
            hset.add(ch);
        return hset.size()==26;
    }
}

// class Solution {
//     public boolean checkIfPangram(String sentence) {
//         // Create a hashSet containing only unique values...
//         Set<Character> hset = new HashSet<>();
//         // Add all elements to hset...
//         for (final char ch : sentence.toCharArray())
//             hset.add(ch);
//         // Check the size of the hset if it is 26 then the string is a pangram...
//         return hset.size() == 26;
//     }
// }