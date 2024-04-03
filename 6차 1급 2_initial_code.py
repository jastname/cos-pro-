import queue

def solution(K, words):
    sk = K
    answer = 0
    if words:
        answer = 1
    for i in words:
        w_len = len(i)
        sk = sk - w_len
        if sk < 0:
            sk = K
            sk = sk - w_len
            answer += 1

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")