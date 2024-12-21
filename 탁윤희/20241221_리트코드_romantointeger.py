class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0 # 최종 결과
        prev = 0 # 이전 문자 값

        for char in reversed(s):
            current = roman_to_int[char] # 현재 로만 문자와 대응하는 정수
            # 현재 값보다 이전 값이 더 크면 total 값에서 뺄셈
            # ex) IV -> 이전 값 V>I이므로 5 -1 = 4가 됨
            if current < prev:
                total -= current
            # 현재 값이 이전 값 이상이면 total에 덧셈
            # ex) II -> 1 + 1 = 2
            else:
                total += current
            # 이전값을 현재 문자로 갱신
            prev = current
        return total