import java.util.Stack;
import java.io.*;

class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        
        dartResult = dartResult.replace("10", "a");
        
        Stack<Integer> st = new Stack<>();
        
        int num = 0;
        for (char d : dartResult.toCharArray()){
            if (Character.isDigit(d)){
                num = Integer.parseInt(String.valueOf(d));
                // System.out.println(num);
            } else if (d == 'a'){
                num = 10;
            } else {
                if (d == 'S'){
                    st.push(num);
                    
                    // System.out.println(st);
                } else if (d == 'D'){
                    st.push((int)Math.pow(num, 2));
                    
                } else if (d == 'T'){
                    st.push((int)Math.pow(num, 3));
        
                } else if (d == '*' && st.size() > 1){
                    int check = st.pop() * 2;
                    int check1 = st.pop() * 2;
                    st.push(check1);
                    st.push(check);
                    
                    
                } else if(d == '*' && st.size() == 1){
                    int check = st.pop() * 2;
                    st.push(check);
                    
                } else if (d== '#' && st.size() > 0){
                    int check = st.pop() * -1;
                    st.push(check);
                }
                
            }
            
        }
        System.out.println(st);
        
        while (!st.isEmpty()){
            answer += st.pop();
        }
        return answer;
    }
}