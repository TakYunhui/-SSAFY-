class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(int i = 1; i <= n; i++){
            answer += check(i, n);
        }

        return answer;
    }
    
    private int check(int checkNum, int n){
        int cnt = checkNum;
        
        while (true) {
            if (checkNum == n){
                return 1;
            } else if (checkNum > n){
                return 0;
            }
            
            cnt ++;
            checkNum += cnt;
        }
        
    }

}
