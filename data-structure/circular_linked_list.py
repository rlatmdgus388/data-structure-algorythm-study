# 어디서든 시작 가능: 어떤 노드에서 시작하더라도 한 바퀴를 돌면 리스트의 모든 노드에 접근가능
# 연속적인 작업에 유리: 예를 들어 게임에서 여러 플레이어가 순서대로 돌아가며 턴을 갖는 경우(A -> B -> C -> A...)나,
#                      CPU 스케줄링(Round-robin)처럼 작업을 반복해서 순환해야 할 때 효율적.


class Node():
    def __init__(self):
        self.data = None
        self.link = None
        

def printNodes(start):
    current = start
    while current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def insertNode(findData, insertData):
    global memory, head, current, pre
    
    if head.data == findData:
        node = Node()
            
    
    
    return


# 전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]


# 메인 코드 부분
if __name__ == "__main__":
    node = Node()               # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    node. link = head           # 원형 리스트가 하나만 존재할 경우 자기 자신을 링크
    memory.append(node)
    
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        node.link = head
        pre.link = node        
        node.link = head
        memory.append(node)
        
    printNodes(head)