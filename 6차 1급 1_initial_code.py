import queue

def solution(n, garden):
    answer = 0
    q = queue.Queue()
    #4방향으로 이동시 이동하는 X,Y좌표
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    
    #시작 위치찾기
    for i in range(n):
        for j in range(n):
            if garden[i][j] == 1:#(i,j)가 1이라면 큐에 좌표입력(0일차 시작)
                q.put((i,j,0))
    
    while q.empty == False: #큐가 비어있지 않다면 반복
        x, y, day = q.get() #1이 있는 위치의 값과 몇일차인지 업데이트

        for i in range(4): #4방향 확인
            next_x = x + dx[i] #다음에 확인할 X좌표
            next_y = y + dy[i] #다음에 확인할 Y좌표
            n_day = day + 1 

            if (0 <= next_x and next_x < n and 0 <= next_y and next_y < n) and (garden[next_x][next_y]==0): 
                #조건(다음에 확인할 x좌표와 y좌표가 0보다 크거나 같고 n보다 작아야함 그리고 다음에 확인할(next_x,next_y)가 0이여야 함)
                garden[next_x][next_y] = 1 #꽃이 핌
                answer = n_day 
                q.put((next_x,next_y,n_day)) #큐에다 새로운 위치와 날짜 입력
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)
#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", 2, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]

ret2 = solution(n2, garden2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")