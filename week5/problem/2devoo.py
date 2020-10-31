# ord('a') == 97
# ord('z') == 122
# chr(97) == a
def solution(encrypted_text, key, rotation):
    answer = ''
    
    # for c, k in zip(encrypted_text, key):
    #     askii = (((ord(c) + ord(k) - 96) - 96) % 26) + 96
    #     print(askii)
    #     answer += chr(askii)
    
    # #answer = answer[-rotation:] + answer[:-rotation]
    # print(answer)


    rotation = rotation % len(encrypted_text)
    encrypted_text = encrypted_text[rotation:] + encrypted_text[:rotation]
    print(encrypted_text)
    for c, k in zip(encrypted_text, key):
        askii = 0
        k = (ord(c) - (ord(k) - 96)) - 96
        if k <= 0:
            askii = k + 122
        else:
            askii = k + 96
        answer += chr(askii)
    print(answer)
    return answer

#print(solution("hellopython", "abcdefghijk", 3) == "qyyigoptvfb")
print(solution("qyyigoptvfb", "abcdefghijk", 3) == "hellopython")
print(solution("bac", "dbc", 3) == "xyz")