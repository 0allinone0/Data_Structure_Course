#두개의 수로 특정값 만들기
def solution(arr, target):
    hash_table = [None]*(target+1)

    #hash table 만들기
    for i in arr:
        if i <= target:
            hash_table[i] = 1

    for i in arr:
        if i >= target:
            continue
        #elif (target - i) == i:
         #   continue
        elif (target - i) in hash_table:
            return True

    return False 

print(solution([1,2,3,4,5,6], 100))


#########
#문자열 해싱
def polynomial_hash(str):
    p = 31
    m = 1_000_000_007
    hash_value = 0
    for char in str:
        hash_value = (hash_value * p + ord(char))% m
    return hash_value

def solution_str(string_list, query_list):
    hash_set = {polynomial_hash(s) for s in string_list}

    result=[]
    for query in query_list:
        query_hash = polynomial_hash(query)
        if query_hash in hash_set:
            result.append(True)
        else:
            result.append(False)
    
    return result



####### 
#실습 5 완주하지 못한 선수
def solution_part(completion, participant):
    dic = {}

    for i in participant:
        if i in dic:
            dic[i] += 1
        else: 
            dic[i] = 1
    
    for i in completion:
        dic[i] -= 1

    for k, v in dic.items():
        if v > 0:
            return k



#실습 7
def solution_7(record):
    user_id_dic = {}
    result = []

    #record task, user_id_dic로 쪼개기 및 업데이트
    for i in record:
        splited = i.split(" ")
        user_id = splited[1]
        
        #유저 id를 key값으로 name을 value
        #Enter 또는 Change일때만 업데이트
        if (splited[0]=="Enter") or (splited[0]=="Change"):
            user_name = splited[2]
            user_id_dic[user_id] = user_name
    
    #result append
    for i in record:
        splited = i.split(" ")
        user_id_2 = splited[1]
        task = splited[0]

        find_user_name = user_id_dic[user_id_2]
        if task == "Enter":
            result.append(f"{find_user_name}님이 들어왔습니다.")

        elif task == "Leave":
            result.append(f"{find_user_name}님이 나갔습니다.")
    
    return result

test = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

print(solution_7(test))
    