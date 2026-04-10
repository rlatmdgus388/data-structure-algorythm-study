# 큐: 입구와 출구가 따로 있는 원통 형태. 먼저 온 사람이 먼저 나가는 FIFO(First In First Out) 구조이다.
# enQueue: 데이터 삽입, deQueue: 데이터 추출


def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE - 1):
        return False
    elif ((rear== SIZE - 1) and (front == -1)):
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False
    

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False
    

def enQueue(data):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data
    
    
def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[(front + 1) % SIZE]


# 전역 변수 선언
SIZE = int(input("큐 크기를 입력하세요: "))
queue = [None for _ in range(SIZE)]
front = rear = 0


# 메인 코드 부분
if __name__ == "__main__":
    select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택: ").upper()
    
    while (select != 'X'):
        if (select == 'I'):
            data = input("입력할 데이터: ")
            enQueue(data)
            print("큐 상태: ", queue)
            print(f"front: {front}, rear: {rear}")
        elif (select == 'E'):
            data = deQueue()
            print("추출된 데이터: ", data)
            print("큐 상태", queue)
            print(f"front: {front}, rear: {rear}")
        elif (select == 'V'):
            data = peek()
            print("확인된 데이터", data)
            print("큐 상태", queue)
            print(f"front: {front}, rear: {rear}")
        else:
            print("입력이 잘못됨.")
            
        select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택: ").upper()
        
    print("프로그램 종료")