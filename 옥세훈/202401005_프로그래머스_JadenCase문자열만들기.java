import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String new_s = s.toLowerCase();
        String[] arr = new_s.split(" ");
        
        for(int i = 0; i < arr.length; i++){
            String now = arr[i];
            
            if(arr[i].length() == 0){
                answer += " ";
            }
            else {
                answer += now.substring(0,1).toUpperCase();
                answer += now.substring(1, now.length());
                answer += " ";
            }
        }
        
        if (s.substring(s.length()-1, s.length()).equals(" ")){
            return answer;
        }
        
       
        return answer.substring(0, answer.length()-1);
    }
}