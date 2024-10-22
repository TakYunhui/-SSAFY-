class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int t_len = t.length();
        int p_len = p.length();
        
        
        long check = 0;
        long int_p = Long.parseLong(p);
        
        for (int i = 0; i <= t_len - p_len; i++){
            check = Long.parseLong(t.substring(i, i+p_len));
            if (check <= int_p) {
                answer += 1;
            }
        }
        
        return answer;
    }
}