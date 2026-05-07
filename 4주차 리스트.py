"""
class list_ADT:
    def __init__(self, capacity):
        self.capacity = 100
        self.arr = [None] * capacity
        self.size = 0

    def insert(self, pos, e):
        new_list = []
        for i in range(a):
            if a[pos] == i:
                new_list = a[:pos]+e
        print(new_list)
        return new_list

    def delete(self, pos):
        new_a = set(a)
        del_value = set(a[pos])
        for i in range(a):
            if i == a[pos]:
                new_list = list(new_a - del_value)
        print(new_list)
        return new_list
    
    def isEmpty(self):
        if a == None:
            print("It is empty")
        else:
            print("Something is in the list")
        
    def getEntry(self, pos):
        print(a[pos])

    def size(self):
        count = 0
        for i in range(a):
            count += 1
        print(count)
        return count

    def clear(self):
        for i in range(len(a)):
            a.pop()
        print(a)

    def find(self, item):
        for i in range(len(a)):
            if item == a[i]:
                print("There is a item!")
                return i
            else:
                print("Couldn't find it")

    def replace(self, pos, item):
        a[pos] = item
        print(a[pos])

    def sort(self):
        for i in range(len(a)-1):       
            for j in range(len(a) - i):            
                if a[j] > a[j+1]:                
                    a[j], a[j+1] = a[j+1], a[j]  # swap    
        print(a)            
        return a


    def merge(self, lst):
        new_list = a + lst
        print(new_list)
        return new_list

    def display(self):
        print(a)

    def append(self,e):
        list(e)
        new_list = a + e
        print(new_list)
        return new_list

a=list_ADT()


#################
#정적 배열
#상속 받아서 만들것

class static_arr(list_ADT):
    def __init__(self, max):
        self.a = a
        self.max = max
        self.list = [None]*max
    

max_capacity = 10
a = [None]*max_capacity
def append(e):
    for i in range(len(a)):
        if a[i] == None:
            a[i] = e
            break
    return a

def is_Full():
    return a[-1] != None

def count(e):
    count = 0
    for i in range(len(a)):
        if 
"""

a = [1,2,3,4,5] #5개 반복
b = [2,1,2,3,2,4,2,5] #8개 반복
c = [3,3,1,1,2,2,4,4,5,5]  #10개 반복
multiple=0  # 몫
rest = 0   #나머지

def solution(ans, total_q):
    #total 문제 개수에 맞게 리스트 만들기
    a_multiple = total_q // len(a) 
    a_rest = total_q % len(a)
    new_a = a * a_multiple + a[:a_rest]

    b_multiple = total_q //len(b)
    b_rest = total_q % len(b)
    new_b = b * b_multiple + b[:b_rest]
    
    c_multiple = total_q // len(c)
    c_rest = total_q % len(c)
    new_c = c * c_multiple + c[:c_rest]

    ans_multiple = total_q // len(ans)
    ans_rest = total_q % len(ans)
    new_ans = ans* ans_multiple + ans[:ans_rest]

    #정답 카운트
    a_count=0
    b_count=0 
    c_count=0
    for i in range(total_q):
        if new_a[i] == new_ans[i]:
            a_count += 1

    for i in range(total_q):
        if new_b[i] == new_ans[i]:
            b_count += 1

    for i in range(total_q):
        if new_c[i] == new_ans[i]:
            c_count += 1

    #가장 많이 맞춘 사람 반환
    count_list = [a_count, b_count, c_count]
    counted_list = sorted(count_list)
    if counted_list[2] == a_count: 
        return [1]
    elif counted_list[2] == b_count:
        return [2]
    elif counted_list[2] == c_count:
        return[3]
    


print(solution([5], 100))



print(7//2)