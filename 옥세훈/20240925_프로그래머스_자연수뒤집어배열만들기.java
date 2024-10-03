import java.util.Arrays;

class Solution {
    public int[] solution(long n) {
        String check = Long.toString(n);
        int len = check.length();
        int[] answer = new int[len];
        
        for (int i = len - 1; i >= 0; i--) {
            answer[len - 1 - i] = Character.getNumericValue(check.charAt(i));
            
        }
        
        System.out.println(Arrays.toString(answer));
        return answer;
    }
}