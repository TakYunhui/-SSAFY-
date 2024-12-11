import java.util.ArrayList;
import java.util.Comparator;
import java.util.Arrays;

class Solution {
    public ArrayList<Integer> solution(String s) {
        
        ArrayList<Integer> answer = new ArrayList<>();
        s = s.substring(2, s.length());
        
        s = s.substring(0, s.length()-2).replace("},{", "-");
        System.out.println(s);
        
        String str[] = s.split("-");
        System.out.println(Arrays.toString(str));
        
        Arrays.sort(str, new Comparator<String>(){
           public int compare(String o1, String o2){
               return Integer.compare(o1.length(), o2.length());
           }
            
        });
        
        for (String x : str){
            String[] temp = x.split(",");
            
            for(int i=0; i < temp.length; i++){
                int n = Integer.parseInt(temp[i]);
                
                if(!answer.contains(n)){
                    answer.add(n);
                }
            }
        }
        
        
        return answer;
    }
}

// import java.util.ArrayList;
// import java.util.Arrays;
// import java.util.Comparator;
// import java.util.List;

// class Solution {
//     public List<Integer> solution(String s) {
//         // 문자열에서 존재하는 "},{"를 "-"로 치환
//         s = s.substring(2, s.length()- 2).replace("},{", "-");
//         // "-"를 기준으로 배열로 분리
//         String[] sArr = s.split("-");

//         // 배열을 길이를 기준으로 정렬
//         Arrays.sort(sArr, Comparator.comparingInt(String::length));

//         List<Integer> list = new ArrayList<>();

//         // 각 집합을 순회하며 정수로 변환하여 리스트에 추가
//         for (String el : sArr) {
//             String[] check = el.split(",");

//             for (int i = 0; i < check.length; i++) {
//                 int num = Integer.parseInt(check[i]);

//                 // 중복된 값이 없을 때만 리스트에 추가
//                 if (!list.contains(num)) {
//                     list.add(num);
//                 }
//             }
//         }

//         return list;
//     }
// }
// 출처: https://ittrue.tistory.com/526 [IT is True:티스토리]