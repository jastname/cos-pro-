#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(arr, K):
    answer = 0
    nl=[]
    arr.sort()
    arr.reverse()
    for i in range(K):
        n = arr.pop()
        nl.append(n)
        print(nl)
    answer = nl[-1] - nl[0]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")