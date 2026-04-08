# 스택: 한 쪽 끝이 막힌 형태. 삽입과 추출이 한쪽에서만 진행.
# 선입후출(First in Last Out, FILO): 먼저 들어간 것이 나중에 나오는 구조
# 후입선출(Last in First Out, LIFO): 나중에 들어간 것이 먼저 나오는 구조
# 스텍에서 데이터 삽입을 push, 데이터 추출을 pop이라 한다.
# top: 스택에 들어 있는 가장 위의 데이터 위치
# 스텍은 크기가 고정되어 있다.


def isStackFull():
    global SIZE, stack, top
    if (top >= (SIZE - 1)):
        return True
    else:
        return False
    

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False
    
    
def push(data):
    global SIZE, stack, top
    if isStackFull():
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data
    

def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print("스택이 비었습니다.")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data
    

def peek():
    global SIZE, stack, top
    if isStackEmpty:
        print("스택이 비었습니다.")
        return None
    return stack[top]


# 전역 변수 선언
SIZE = int(input("스택 크기를 입력하세요: "))
stack = [None for _ in range (SIZE)]


# 메인 코드
if __name__ == "__main__":
    select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택: ").upper()
    
    while (select != 'X'):
        if (select == 'I'):
            data = input("입력할 데이터: ")
            push(data)
            print("스택 상태: ", stack)
        elif (select == 'E'):
            data = pop()
            print("추출된 데이터: ", data)
            print("스택 상태", stack)
        elif (select == 'V'):
            data = peek()
            print("확인된 데이터", data)
            print("스택 상태", stack)
        else:
            print("입력이 잘못됨.")
            
        select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택: ").upper()
        
    print("프로그램 종료")
            
            