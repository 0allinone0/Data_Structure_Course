class Circular_Queue:
    def __init__(self, max_size):
        self.front = 0
        self.rear = 0
        self.max_size = max_size
        self.items = [None] * max_size

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
        
    def is_full(self):
        return self.front % self.max_size == (self.rear+1)%self.max_size 
    
    def enqueue(self, x):
        if not self.is_full():
            self.rear = (self.rear+1) % self.max_size
            self.items[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            print("it is empty")
        else:
            self.front = (self.front+1) % self.max_size
            value = self.items[self.front]
            self.items[self.front] = None
            return value

    def peek(self):
        if not self.is_empty():
            return self.items[(self.front+1)%self.max_size]
        
    def size(self):
        return (self.rear - self.front + self.max_size) % self.max_size
    
    def clear(self):
        for i in range(self.max_size):
            if self.front == self.rear:
                break
            else:
                self.dequeue()

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        elif self.front > self.rear:
            out = self.items[self.front+1:self.max_size] + self.items[0:self.rear+1]
        print(out)


q = Circular_Queue(10)
for i in range(8): q.enqueue(i)
q.display()



def yosefus(N, K):
    q = Circular_Queue(N+1)
    for i in range(N):
        q.enqueue(i+1)

    #요소 한개 남을때까지
    while (q.size() != 1):
        #K-1개 뒤로 보내기
        for i in range(K-1):
            tmp = q.dequeue()
            q.enqueue(tmp)

        #맨앞 요소 삭제
        q.dequeue()
    
    return q.peek()

#요세푸스 확인
a=yosefus(7,3)
print(a)



class Deque(Circular_Queue):
    def __init__(self, max_size):
        super().__init__(max_size) # 부모생성자 호출할때

    def add_front(self, x):
        if not self.is_full():
            self.items[self.front] = x
            self.front = (self.front-1 + self.max_size)%self.max_size

    def delete_rear(self):
        delete = self.items[self.rear]
        self.items[self.rear] = None
        self.rear = (self.rear-1 + self.max_size) %self.max_size
        return delete
    
    def get_rear(self):
        return self.items[self.rear]
    
    def delete_front(self):
        self.dequeue()
    
    def get_front(self):
        return self.peek()
    
    def add_rear(self, x):
        self.enqueue(x)

    def is_Empty(self):
        return self.is_empty()
    


dq = Deque(10)

for i in range(9):
    if i%2==0 : dq.add_rear(i)
    else: dq.add_front(i)

dq.display()

for i in range(2): dq.delete_front()
dq.display()

for i in range(3): dq.delete_rear()
dq.display()

for i in range(9,14): dq.add_front(i)
dq.display()