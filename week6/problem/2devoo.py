def solution(s):
    answer = []
    r_zero, count = 0, 0
    no_zero = ""
    while s != "1":
        for i in s:
            if i == "1":
                no_zero += "1"

        r_zero += len(s) - len(no_zero)
        s = format(len(no_zero), 'b')
        no_zero = ""
        count += 1
        
    answer = [count, r_zero]
    
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))