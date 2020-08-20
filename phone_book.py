def solution(phone_book):
    
    for a in range(len(phone_book)):
        k1 = len(phone_book[a])
        
        for b in range(a+1, len(phone_book)):
            k2 = len(phone_book[b])
            
            if phone_book[a] in phone_book[b][:k1] or phone_book[b] in phone_book[a][:k2] :
                return False
    return True

###############################################
def solution(phone_book):
    phone_book.sort()
    for a in range(len(phone_book)-1):
        if phone_book[a] in phone_book[a+1] :
            return False
    return True
