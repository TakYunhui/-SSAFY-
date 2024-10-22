class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String str = Integer.toString(n, 3);
        StringBuilder sb = new StringBuilder(str);
        String reverse_str = sb.reverse().toString();
        
        answer = Integer.parseInt(reverse_str, 3);
        return answer;
    }
}