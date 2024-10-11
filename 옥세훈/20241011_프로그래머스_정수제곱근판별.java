class Solution {
    public long solution(long n) {
        long answer = 0;
        long num = 1;
        
        long temp = 0;
        while(true) {
            if (temp == n) {
                answer = num * num;
                break;
            } else if (temp > n) {
                answer = -1;
                break;
            }
            
            temp = num * num;
            num ++;
        }
        return answer;
    }
}