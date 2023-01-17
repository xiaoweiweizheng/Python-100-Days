def is_palindrome(num):
    ori_num = num
    rev_num = 0
    while num>0:
        rev_num = rev_num*10 + num%10
        num //= 10
    
    return rev_num == ori_num

if __name__ == "__main__":
    print(is_palindrome(121))