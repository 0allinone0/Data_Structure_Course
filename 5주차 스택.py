class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def is_Empty(self):
        return self.top == -1 #스택에 있는 top값이 -1이면 비어있는 것

    def is_Full(self):
        return self.top == self.capacity - 1
    
    def push(self, e):
        if not self.is_Full():
            self.top += 1
            self.array[self.top] = e
        else:
            pass
    
    def pop(self):
        e = self.array[self.top]
        self.array[self.top] = None
        self.top -= 1
        return e

    def peek(self):
        if not self.is_Empty():
            return self.array[self.top]
    
    def size(self):
        return self.top + 1
    
    def __str__(self):       #그냥 스택을 프린트하면 메모리 값이 나옴. 그래서 이 함수를 써서 스택에 있는 값 호출
        return str(self.array[0:self.top+1])


a = Stack(10)

a.push(5)
a.push(10)
a.push(18)
print(a.__str__())
print(a.size())
print(a.peek())


##############
#회문 검사 함수

def palindrome(word):
    a = Stack(len(word))
    for i in word:
        a.push(i)

    for i in word:
        if i != a.pop():
            return False
    return True

a = palindrome("lllll")
print(a)


#########
#10진수를 2진수로
def ten_to_two(num):
    now_num = num
    a=Stack(100)     #Stack 생성

    #나머지 구해서 stack에 저장하는 연산
    while(now_num != 0):
        a.push(now_num%2)
        now_num = now_num//2

    final = []   #pop하여 final에 저장
    for i in range(a.size()):
        final.append(a.pop())

    return final

a = ten_to_two(13)
print(a)



#괄호 검사
def check_bracket(s):
    a = Stack(10)
    for i in s:
        if i == "(":
            a.push(i)
        else:
            a.pop()

    return a.is_Empty()   #비어 있다면 짝이 맞는것임


a= "()(((())()"
print(check_bracket(a))

#괄호 검사2
def check_bracket2(s):
    a=Stack(100)
    for i in s:
        if i == "[" or i == "{" or i == "(":
            a.push(i)
        else:
            if i == ")" and a.peek() == "(":
                a.pop()
            elif i =="]" and a.peek() == "[":
                a.pop()
            elif i == "}" and a.peek() == "{":
                a.pop()
        
    return a.is_Empty()

print(check_bracket2("{A[(i+1)]=0;}"))



##########
#계산기 만들기
#후위 표기가 되어있는 계산기
def eval_Post(s):
    a = Stack(100)
    for i in s:
        
        if i == "/":
            first = int(a.pop())
            second = int(a.pop())
            cal = second / first
            a.push(cal)
        elif i == "*":
            first = int(a.pop())
            second = int(a.pop())
            cal = second * first
            a.push(cal)
        elif i == "-":
            first = int(a.pop())
            second = int(a.pop())
            cal = second - first
            a.push(cal)
        elif i == "+":
            first = int(a.pop())
            second = int(a.pop())
            cal =second+ first
            a.push(cal)
        else:   #숫자일때는 stack에 저장
            a.push(i)
    return a.pop()

print(eval_Post("832+1-/")) 
