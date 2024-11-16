class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        
        int[] di = {0, 1, -1, 0};
        int[] dj = {1, 0, 0, -1};
        
        String check = board[h][w];
        
        int board_i = board.length;
        int board_j = board[0].length;
        
        int hi = 0;
        int wj = 0;
        for (int i=0; i < 4; i++){
            hi = h + di[i];
            wj = w + dj[i];
            
            if (0 <= hi && hi < board_i && 0 <= wj && wj < board_j){
                if (board[hi][wj].equals(check)){
                    answer ++;
                }
            }
        }
        
        return answer;
    }
}