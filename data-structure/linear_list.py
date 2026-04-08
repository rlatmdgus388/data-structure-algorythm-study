# 리스트 생성
lst = [1, 2, 3, 4, 5]

# 데이터 삽입 함수
def insert_data(lst, idx, value):
    lst.append(None)
    
    for loc in range(len(lst) - 1, idx, -1):
        lst[loc] = lst[loc - 1]
    lst[idx] = value
    
    return lst

# 데이터 삭제 함수
def delete_data(lst, idx):
    lst[idx] = None
    for i in range(idx, len(lst) - 1):
        lst[i] = lst[i + 1]   
        
    del(lst[-1])
    
    return lst


delete_data(lst, 2)
print(lst)