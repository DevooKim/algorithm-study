def solution(encrypted_text, key, rotation):
    table = 'abcdefghijklmnopqrstuvwxyz'

    unrotation = encrypted_text[rotation:] + encrypted_text[:rotation]

    answer = ''
    for i, k in enumerate(key):
        weight = table.index(k) + 1
        answer += table[(table.index(unrotation[i]) - weight)]
    return answer

# solution('hellopython','abcdefghijk',3)
solution('qyyigoptvfb','abcdefghijk',3)
