class Node:
    def __init__(self, data, link =None):
        self.data = data
        self.link = link

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top == None
    
    def push(self, e):
        n = Node(e, self.top)
        n.link = self.top
        self.top = n
        self.count += 1 

    def pop(self):
        n = self.top
        self.top = n.link
        self.count -= 1
        return n.data
    
    def peek(self):
        n = self.top
        return n.data
    
    def size(self):
        return self.count
    
    def clear(self):
        self.top = None
            
a = Stack()
for i in range(10):
    a.push(i)

print(a.size())

class List:
    def __init__(self, head):
        self.head = None

    def get_entry(self, pos):
        if pos < 0:     #pos는 음수면 안됨
            return None
        n = self.head
        while (n != None and pos>0):
            n = n.link  #다음 노드로 이동
            pos -= 1

        return n

    def insert(self, pos, e):
        before = self.getNode(pos-1)
        if before == None: #맨 앞에다가 할 때
            self.head = Node(e, self.head)
        else:
            n = Node(e, before.link)
            before.link = n

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:   #맨 앞 삭제시
            self.head = self.head.link

        else:
            before.link = before.link.link

    def is_empty(self):
        return self.head == None
    
    def size(self):
        n = self.head
        count = 0
        while (self.head == None):
            n.link = self.head
            count += 1

        return count
    
class Queue:
    def __init__(self, tail):
        self.tail = None

    def is_empty(self):
        return self.tail == None
        
    def enqueue(self, data):
        n = Node(data, None)
        if self.is_empty():  #처음으로 넣을때
            n.link = n
            self.tail = n
        else:   
            n.link = self.tail.link
            self.tail.link = n
            self.tail = n

    def dequeue(self):
        if not self.is_empty():
            data = self.tail.link.data
            if self.tail.link == self.tail:  #하나의 항목만 가질 때
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
            
    def size(self):
        if self.is_empty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count


class double_link:
    def __init__(self, data, prev=None, next= None):
        self.data = data
        self.prev = prev
        self.next = next


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None
    
    def add_front(self, data):
        n = double_link(data, None, self.front)   #맨 앞에다가 add하기 때문에 prev는 None이 되어야함
        if self.is_empty():
            self.front = n
            self.rear = n    #front와 rear 둘다 n
        else:
            self.front.prev = n
            self.front = n

    def add_rear(self, data):
        n = double_link(data, self.rear, None)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n

    def delete_front(self):
        if not self.is_empty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:     #하나만 있을 경우
                self.rear = None
            else:
                self.front.prev = None
            return data

    def delete_rear(self):
        if not self.is_empty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:   #노드가 하나이면
                self.front = None
            else:
                self.rear.next = None
            return data
    
    def size(self):
        count = 0
        n = self.front
        while (n.next != None):
            n = n.next
            count += 1
        return count
    
    def display(self):
        dis_list = []
        if not self.is_empty():
            n = self.front
            while (n != None):
                dis_list.append(n.data)
                n = n.next
        else:
            print("It is empty")
        print(dis_list)


dq = Deque()

for i in range(9):
    if i%2==0 : dq.add_rear(i)
    else: dq.add_front(i)

dq.display()

for i in range(2): dq.delete_front()
for i in range(3): dq.delete_rear()
dq. display()

for i in range(9,14): dq.add_front(i)
dq.display()