class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arr = s.split("");
        int idx = 0;
        
        for (String a : arr){
            if (a.contains(" ")){
                idx = 0;
            } else {
                idx ++;
            }
            if (idx % 2 == 0){
                answer += a.toLowerCase();
            } else{
                answer += a.toUpperCase();
            }
        }
        
        return answer;
    }
}