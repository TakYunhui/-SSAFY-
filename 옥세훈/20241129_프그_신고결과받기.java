import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        
        HashMap<String, HashSet<String>> map = new HashMap<>();
        HashMap<String, Integer> mapIdx = new HashMap<>();
        
        for (int i=0; i<id_list.length; i++){
            String name = id_list[i];
            map.put(name, new HashSet<>());
            mapIdx.put(name, i);
        }
        
        for (String s : report){
            String[] str = s.split(" ");
            String from = str[0];
            String to = str[1];
            map.get(to).add(from);
        }
        
        for(int i=0; i<id_list.length; i++){
            HashSet<String> send = map.get(id_list[i]);
            if (send.size() >= k) {
                for (String name: send) {
                    answer[mapIdx.get(name)] ++;
                }
            }
        }
        
        
        
        return answer;
    }
}