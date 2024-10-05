class Solution {
    public int[] solution(String s) {
        int cnt = 0;      // 변환 횟수
        int zeroCount = 0; // 0의 개수
        
        while (true) {
            if (s.equals("1")) {
                break; // 문자열이 "1"이면 종료
            }
            
            // 0의 개수 세기
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    zeroCount++;
                }
            }
            
            // 0 제거
            s = s.replace("0", ""); // 빈 문자열로 대체
            cnt++; // 변환 횟수 증가
            
            // 현재 문자열의 길이를 2진수로 변환
            s = Integer.toBinaryString(s.length());
        }
        
        // 결과 배열 생성
        return new int[]{cnt, zeroCount};
    }
}
