import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        Queue<Character> q = new LinkedList<>();
        
        for (int i = 0; i < s.length(); i++) {
            q.add(s.charAt(i));
        }
        
        boolean flag = false;
        char x = q.poll();
        
        char check = ' ';
        int x_num = 1;
        int y_num = 0;
        
        while (q.size() > 0){
            if (flag && q.size() > 1) {
                x = q.poll();
                check = q.poll();
            } else {
                check = q.poll();
            }
            
            
            if (check == x) {
                x_num += 1;
            } else {
                y_num += 1;
            }
            
            if (x_num == y_num){
                answer ++;
                x_num = 1;
                y_num = 0;
                flag = true;
            } else{
                flag = false;
            }
            
            
        }
        
        if (!flag && x_num > y_num){
            answer ++;
        }
        
        return answer;
    }
}