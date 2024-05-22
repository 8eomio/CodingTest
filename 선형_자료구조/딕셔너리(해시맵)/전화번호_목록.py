def solution(phone_book):
    answer = True
    phone_book.sort()
    for i, num in enumerate(phone_book[:-1]):
        if phone_book[i+1].startswith(num):
            answer =False
    return answer
