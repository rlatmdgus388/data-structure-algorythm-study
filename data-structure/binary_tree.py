# 트리: 나무를 거꾸로 뒤집어 놓은 듯한 형태를 가진 자료구조로, 데이터 간의 계층적 관계(부모-자식 관계)를 표현하는 데 특화된 비선형 자료구조이다.
# 컴퓨터의 디렉터리(폴더) 구조, 조직도, 인공지능의 의사결정 트리 등에 활용
# 노드(Node): 트리를 구성하는 각각의 데이터 요소
# 루트 노드(Root Node): 트리의 가장 꼭대기에 있는 시작 노드입니다. 트리는 단 하나의 루트 노드만 가짐.
# 레벨(level): 루트 노드 층부터 밑에 층 순으로 레벨 0, 1, 2..이라 한다.
# 간선(Edge/Link): 노드와 노드를 연결하는 선
# 깊이(Depth): 루트 노드에서 특정 노드까지 도달하기 위해 거쳐야 하는 간선의 수
# 높이(Height): 루트 노드에서 가장 깊숙히 있는 리프 노드까지의 최대 깊이
# 부모 노드(Parent Node) & 자식 노드(Child Node): 간선으로 연결된 상하 관계. 위쪽이 부모, 아래쪽이 자식
# 형제 노드(Sibling Node): 같은 부모를 가진 노드들
# 리프 노드(Leaf Node / Terminal Node): 자식 노드가 하나도 없는 가장 밑바단의 노드
# 차수(degree): 자식 노드의 개수. 트리의 차수는 차수가 가장 높은 노드를 기준으로 정함.
# 이진 트리(binary tree): 모든 노드가 자식이 2개 이하로 구성돼있는 트리

# 이진 트리의 종류
# 1. 포화 이진 트리(full binary tree): 모든 노드가 꽉 차 있는 상태의 트리. 
#   a. 노드 개수: 2^(높이 + 1) - 1
#   b. 보통 루트 노드부터 아래로, 왼쪽 -> 오른쪽 으로 번호를 부여함.
# 2. 완전 이진 트리(complete binary tree): 번호를 부여한 순서로 노드를 배치
#   a. 마지막 레벨을 제외한 모든 레벨이 노드로 꽉 차 있어야 한다.즉, 깊이가 h라면 h-1 레벨까지는 모든 노드가 존재해야함.
#   b. 마지막 레벨의 노드는 반드시 왼쪽부터 차례대로 채워져야 한다. 오른쪽은 비어 있을 수 있지만, 중간에 빈칸이 생기면 완전 이진 트리가 아님.
# 3. 편향 이진 트리(skewed binary tree): 모든 노드가 오른쪽이나 왼쪽으로 연결된 트리.

# 이진트리는 왼쪽과 오른쪽 링크가 있는 이중 연결 리스트 구조로 만들 수 있다.
class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left= node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

print(node1.data, end=' ')
print()
print(node1.data, node1.right.data, end=' ')
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data, end=' ')


# 이진 트리의 순회: 이진 트리의 노드를 한 번씩 방문하는 것
# 데이터를 검색할 때 더 효율적으로 검색하기 위해 고안
# 종류
# 1. 전위 순회: 노드의 데이터를 먼저 처리함.
#   a. 루트에서 시작하여 데이터 처리 -> 왼쪽 서브 트리 -> 오른쪽 서브 트리 순서로 순회

