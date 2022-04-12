def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        key1 = phone_book[i]
        key2 = phone_book[i+1]
        if(key1 == key2[:len(key1)]):
            return False
    return True