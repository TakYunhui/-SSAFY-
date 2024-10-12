class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        
        String new_x = Integer.toString(x);
     
        int check = 0;
        for(char c : new_x.toCharArray()) {
            check += Character.getNumericValue(c);
        }
        
        if(x % check == 0){
            answer = true;
        } else {
            answer = false;
        }
        return answer;
    }
}