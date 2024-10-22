import java.util.Arrays;

class Solution {
    public String solution(String phone_number) {
        String answer = "";
        
        // # list로 변환
        // # 길이가 4면 그대로 반환
        // # 아니면 범위를 활용하여 -4 해서 바꿔버림
        // # 그리고 다시 돌면서 더해주고 출력
            
        if (phone_number.length() == 4){
            return phone_number;
        }
        
        String[] arr = phone_number.split("");
        
        for (int i = 0; i < arr.length - 4; i++){
            arr[i] = "*";
        }
        
        answer = String.join("", arr);
        
        return answer;
    }
}