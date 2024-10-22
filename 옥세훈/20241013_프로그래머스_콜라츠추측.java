class Solution {
    public int solution(int num) {
        int answer = 0;
        int cnt = 0;
        
        while (true) {
            if (num == 1){
                answer = cnt;
                break;
            } else if (cnt >= 500) {
                answer = -1;
                break;
            }
            
            if (num % 2 == 0) {
                num = num / 2;
            } else if (num % 2 == 1) {
                num = num * 3 + 1;
            }
            
            cnt += 1;
        }
        
        return answer;
    }
}