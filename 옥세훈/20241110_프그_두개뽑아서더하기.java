import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};
        Set<Integer> arr = new HashSet<>();
        
        for (int i = 0; i < numbers.length; i++){
            for (int j = i+1; j < numbers.length; j++){
                arr.add(numbers[i] + numbers[j]);
            }
        }
        
        answer = new int[arr.size()];
        
        
        int idx = 0;
        for (int i : arr) {
            answer[idx] = i;
            idx ++;
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}