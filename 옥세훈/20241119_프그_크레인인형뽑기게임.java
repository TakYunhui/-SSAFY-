import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        
        for (int m : moves){
            
            for (int j=0; j<board.length; j++){
                int check = board[j][m-1];
                // System.out.println(check);
                
                if (check != 0){
                    if(stack.size() > 0 && stack.peek() == check){
                        stack.pop();
                        answer += 2;
                    } else {
                        stack.add(check);
                    }
                    
                    board[j][m-1] = 0;
                    break;
                }
                
                
            }
            
            
        }
        
        return answer;
    }
}