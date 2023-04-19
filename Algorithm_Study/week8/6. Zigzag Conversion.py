class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: #예외 처리 - 한 줄이면 그대로 반환
            return s
        
        store = [[] for _ in range(numRows)] # numRows만큼 재배치할 행을 초기화
        answer = ''

        i = 0 # 문자 넣어 줄 행의 값
        toggleDown = True

        for x in s:
            store[i].append(x)
            if i == 0: # 현재 위치가 첫 번째 행이면 아래로 
                toggleDown = True
            elif i == numRows - 1: # 현재 위치가 끝 행이면 위로
                toggleDown = False
            if toggleDown:
                i += 1
            else:
                i -= 1

        for i in range(numRows):
            answer += ''.join(store[i])

        return answer



"""
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

"""