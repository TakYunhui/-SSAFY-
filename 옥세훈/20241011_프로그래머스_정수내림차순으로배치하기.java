
class Solution {
    public long solution(long n) {
        long answer = 0;
        Character[] arr = new Character[new_n.length()];
        
        for (int i=0; i < new_n.length(); i++){
            arr[i] = new_n.charAt(i);
        }
        
        // char 형태로도 숫자들은 크기 비교를 통해 정렬할 수 있다.
        // 자바에서 int 형 배열은 역정렬하는 함수가 없어서 직접 만들어야 한다.
        Arrays.sort(arr, Collections.reverseOrder());
        
        StringBuilder answer = new StringBuilder();
        for (char c : arr) {
            answer.append(c);
        }
        return answer;
    }
}