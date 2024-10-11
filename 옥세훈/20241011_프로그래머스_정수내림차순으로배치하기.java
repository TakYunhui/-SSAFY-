import java.util.Arrays;
import java.util.Collections;

class Solution {
    public long solution(long n) {
        // 정수를 문자열로 변환
        String new_n = String.valueOf(n);
        // 각 자리수를 저장할 배열 생성
        Character[] arr = new Character[new_n.length()];

        // 각 자리수를 배열에 추가
        for (int i = 0; i < new_n.length(); i++) {
            arr[i] = new_n.charAt(i);
        }

        // 배열을 내림차순으로 정렬
        Arrays.sort(arr, Collections.reverseOrder());

        // 정렬된 문자열을 정수로 변환
        StringBuilder answer = new StringBuilder();
        for (char c : arr) {
            answer.append(c);
        }

        return Long.parseLong(answer.toString()); // 정수로 반환
    }

}
