# 원형 큐: 큐의 처음과 끝이 연결된 구조. 한 줄에 차례대로 데이터가 입, 출력되는 순차 큐보다 효율적
# 순차 큐처럼 배열로 구현하되 큐의 끝에 다다르면 다시 처음으로 이어지게 연결
# 순차 큐는 데이터를 삭제 후 삽입할 시 데이터들을 앞으로 옮겨야하는 비효율 발생. 이에 대한 대안이 원형 큐이다.


def isQueueFull():
    global SIZE, rear, front, queue
    if ((rear+1) % SIZE == front):
        return True
    else:
        return False
    
    
def isQueueEmpty():
    global SIZE, rear, front, queue
    if (front == rear):
        return True
    else:
        return False
    

def enQueue(data):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data
    
    
def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % SIZE
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
front = rear = -1


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
