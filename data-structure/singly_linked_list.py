# 단순 연결 리스트 생성
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
        
def printNodes(start):          # 노드 출력 함수
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()


def insertNode(findData, insertData):
    global memory, head, current, pre
    
    if head.data == findData:   # 첫 번째 노드에 삽입인 경우
        node = Node()
        node.data = insertData
        node.link = head    # 새 노드의 link를 다음 노드로 연결
        head = node         # head를 새 노드로 변경
        return
        
    # 중간 노드에 삽입하는 경우
    current = head      # 위 if문을 통과 -> 첫 번째 노드에 삽입이 아닌 경우
    while current.link != None:
        pre = current
        current = current.link          # currnet를 다음 노드로 한 칸 이동
        if current.data == findData:    # current가 삽입하려는 데이터의 위치이면
            node = Node()
            node.data = insertData
            node.link = current         # 새 노드의 link를 current에 연결
            pre.link = node             # 새 노드 이전 link를 새 노드에 연결
            return
        
    # 마지막 노드 삽입
    node = Node()                       # 반복문을 전부 돌때까지 findData를 못찾을 시, 맨 뒤에 새 노드 생성.
    node.data = insertData
    current.link = node


def deleteNode(deleteData):
    global memory, head, current, pre
    
    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
        
# 검사 후 이동(마지막 노드 검사 못함)
def findNode(findData):
    global memory, head, current, pre
    
    current = head
    while current.link != None:
        if current.data == findData:
            return current
        else:
            current = current.link


# 이동 후 검사(전 노드 검사 가능)
def findNode(findData):
    global memory, head, current, pre
    
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    return Node()


memory = []     # 전역 변수 선언
head, current, pre = None, None, None
dataArray = [1, 2, 3, 4, 5]

if __name__=="__main__":
    node = Node()               # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)
    
    for data in dataArray[1:]:  # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
        
    printNodes(head)
    