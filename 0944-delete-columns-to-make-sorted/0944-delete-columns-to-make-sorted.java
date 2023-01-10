class Solution {
    public int minDeletionSize(String[] strs) {
        int rows=strs.length;
        int col=strs[0].length();
        int ans=0;
        for(int i=0;i<col;i++)
        {
            for(int j=1;j<rows;j++)
            {
                if (strs[j].charAt(i) < strs[j - 1].charAt(i))
                {
                    ans++;
                    break;
                }
            }
        }
        return ans;
        
    }
}