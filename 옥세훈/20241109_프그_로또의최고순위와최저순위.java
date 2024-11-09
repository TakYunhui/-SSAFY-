class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        
        
        int[] ranks = new int[] {6,6,5,4,3,2,1};
        int cnt_0 = 0;
        
        for (int i=0; i < lottos.length; i++){
            if(lottos[i] == 0){
                cnt_0 ++;
            }
        }
        
        int ans = 0;
        for (int i=0; i<win_nums.length; i++){
            for (int j=0; j<lottos.length; j++){
                if (win_nums[i] == lottos[j]) {
                    ans ++;
                }
            }
        }
        
        answer[0] = ranks[ans+cnt_0];
        answer[1] = ranks[ans];
        
        return answer;
    }
}