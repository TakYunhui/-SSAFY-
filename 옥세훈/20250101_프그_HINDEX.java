import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int len = citations.length;
        Arrays.sort(citations);
        
        int minNum = citations[0];
        if (minNum >= len){
            return len;
        }
        
        for (int i=0; i<len; i++){
            int cnt = 0;
            
            for (int j=i; j<len; j++){
                if(citations[i] < citations[j]){
                    cnt += 1;    
                }
        
            }
    
            if (cnt >= citations[i]){
                answer = cnt;
            }
        }
        
        return answer;
    }
}