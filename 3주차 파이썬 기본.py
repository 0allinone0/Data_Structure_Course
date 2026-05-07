text = "Python 3.10 is fun, let's code!"

#다 거꾸로 만들기
print(text[::-1])

#단어 단위 뒤집기
a = text.split(" ")
print(a)
print(" ".join(a[::-1]))

#단어내에 글자 뒤집기
b = text.split(" ")
def reverse_in_word(text_list):
    new_list = [None for _ in range(len(text_list))]
    
    for i in range(len(text_list)):
        new_list[i] = text_list[i][::-1]
    
    return " ".join(new_list)
print(reverse_in_word(b))



#리스트 회전
a = [1, 2, 3, 4, 5]

def right_rotate(test_list, n):
  new_list = [None for _ in range(len(test_list))] #새로운 배열 만들기

  for i in range(len(test_list)):
       new_list[i] = test_list[i-n]  #새로운 배열에 값 추가

  return new_list

print(right_rotate(a, 2))



#Dictionary
#두 문자열이 아나그램인지 확인
def anagram(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

print(sorted('listen'))  #문자열을 알파벨순으로 리스트 형태로 저장
print(anagram('listen', 'silent'))

def is_anagram(a, b):
    a_dict = dict()
    b_dict = dict()
    if len(a) != len(b):
        return False
    else: 
        for i in a:
            if i in a_dict:
                a_dict[i] += 1
            else: 
                a_dict[i] = 0
        
        for i in b:
            if i in b_dict:
                b_dict[i] += 1
            else:
                b_dict[i] = 0
        
        #if


#lambda 함수
#길이가 4이상인 단어를 모두 대문자로 변환하여 출력하시오
def up_4_upper(words):
    #filter + lambda 알파벳 수가 4개 이상인 단어 필터
    filtered_words = filter(lambda x: len(x) >= 4, words)

    #map + lambda로 대문자 리스트로 변환
    result = list(map(lambda x: x.upper(), filtered_words))
    return result

words = ["banna", "apple", "hi", 'bye', 'cat', 'watermelon']
print(up_4_upper(words))


#클래스
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14 * self.__radius**2
    
    def get_circumstance(self):
        return 2 * 3.14 *self.__radius
    

a = Circle(10)
print(a.get_area())
print(a.get_circumstance())
        