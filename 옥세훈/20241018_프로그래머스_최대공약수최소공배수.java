class Solution {
    
    public int getGcd(int a, int b) {
            if (b == 0) {
                return a;
            } else {
                return getGcd(b, a % b);
            }
        }
    
    public int[] solution(int n, int m) {
        
        int gcd = getGcd(n, m);
        int lcm = n * m / gcd;
        int[] answer = new int[] {gcd, lcm};
        
        return answer;
    }
}