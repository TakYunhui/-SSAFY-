class Solution {
    public String solution(String s) {
        String[] tmp = s.split(" ");
        int max, min, n;
        min = max = Integer.parseInt(tmp[0]);
            
        for (int i = 1; i < tmp.length; i++){
                n = Integer.parseInt(tmp[i]);
            if(min > n) min = n;
            if(max < n) max = n;
        }
        
        
        return min + " " + max;
    }
}