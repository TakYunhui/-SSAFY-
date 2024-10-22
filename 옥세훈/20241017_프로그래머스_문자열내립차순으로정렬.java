import java.util.Arrays;
import java.util.Collections;
import java.util.List;


class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] arr = s.split("");
        Arrays.sort(arr);
     
        List<String> ls = Arrays.asList(arr);
        Collections.reverse(ls);
        
        for (String c : ls){
            answer += c;
        }
        
        
        return answer;
    }
}