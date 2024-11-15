import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        // 같은 이름의 완주자가 있을 수 있기 때문에 map 사용
        Map<String, Integer> map = new HashMap<>();

        for (String s : participant) {
            // key가 없는 경우 1, 있을 경우 +1
            map.put(s, map.getOrDefault(s, 0) + 1);
        }

        for (String s : completion) {
            // 완주한 사람의 1명씩 제거
            map.put(s, map.get(s) - 1);
        }

        for (String s : map.keySet()) {
            // 완주하지 못한 사람
            if (map.get(s) > 0) {
                answer = s;
                break;
            }
        }

        return answer;
    }
}
