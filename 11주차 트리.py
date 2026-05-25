def solution(a, b):
    #a: a번 참가자
    #b: b번 참가자
    result = 0
    while (a != b):
        a = (a+1)//2
        b = (b+1)//2
        result += 1
    return result

print(solution(4, 7))


########
#트리 순회
class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#전위 순회
def preorder(n):
    if n is not None:
        print(n.data, end="")
        preorder(n.left)
        preorder(n.right)

#중위 순회
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end="")
        inorder(n.right)

#후위 순회
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end="")


# 원형큐 ADT
MAX_QSIZE = 100
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item


    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front + 1:self.rear + 1]  # 슬라이싱
        else:
            out = self.items[self.front + 1:MAX_QSIZE] + self.items[0:self.rear + 1]  # 다음 줄에 계속 + 슬라이싱
        print("[f=%s, r=%d] ==> "%(self.front, self.rear), out)


#Level 순회
def level_order(n):
    #입력으로 root 노드 받음
    queue = CircularQueue() #큐 생성
    queue.enqueue(n) #최초에 큐에는 루트 노드만 들어있음.
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end="")
            queue.enqueue(n.left)
            queue.enqueue(n.right)


#노드 개수
def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)

#단말 노드의 수
def count_leaf(n):
    if n is None:    #노드가 없으면 단말노드 아님
        return 0   
    elif n.left is None and n.right is None:   #해당 노드의 왼쪽, 오른쪽 자식 노드가 모두 없으면 단말노드
        return 1
    else:    #단말노드가 아닐 시
        return count_leaf(n.left) + count_leaf(n.right)

#트리의 높이 
def get_height(n):
    if n is None:    #노드가 비어있으면 높이는 0
        return 0
    else:
        return 1 + max(get_height(n.left), get_height(n.right))   #현재 노드의 높이 1 + 왼쪽 서브트리 또는 오른쪽 서브트리의 높이 중 큰것
    

#두 트리 같은지 비교
def comparation(n1, n2):
    if n1 is None and n2 is None:     #두 트리가 모두 비어있으면
        return True
    elif n1 is not None and n2 is not None:  #두 해당 노드가 있으면
        if n1.data != n2.data:  #해당 노드의 값이 다르면
            return False
        else:  #해당 노드의 값이 같으면 왼쪽과 오른쪽 자식 노드 비교
            return comparation(n1.left, n2.left) and comparation(n1.right, n2.right)  
    else:
        return False