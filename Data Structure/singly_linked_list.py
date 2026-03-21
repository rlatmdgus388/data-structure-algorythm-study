# 단순 연결 리스트 생성
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.node != None:
        crrent = current.link
        print(current.data, end = ' ')
    print()
    
