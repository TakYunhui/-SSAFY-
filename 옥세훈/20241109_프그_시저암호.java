class Solution {
    public String solution(String s, int n) {
        String answer = "";
        
        for (char c : s.toCharArray()) {
            if (c == ' '){
                answer += ' ';
            } else {
                int check = (int)c + n;
                // System.out.println(check);
                
                if (Character.isUpperCase(c) && check > 90){
                    int num = 64 + (check - 90);
                    answer += (char)num;
                } else if (Character.isLowerCase(c) && check > 122){
                    int num1 = 96 + (check - 122);
                    answer += (char)num1;
                } else {
                    answer += (char)check;
                }
                
            }
        }
        
        return answer;
    }
}