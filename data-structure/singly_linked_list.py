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
        node.link = head
        head = node
        return
        
    # 중간 노드에 삽입하는 경우
    current = head
    while current.link == None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    # 마지막 노드 삽입
    node = Node()
    node.data = insertData
    current.link = node
            


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
    