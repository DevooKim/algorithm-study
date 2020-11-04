def solution(encrypted_text, key, rotation):
    table = 'abcdefghijklmnopqrstuvwxyz'

    if len(encrypted_text) == 1:
        weight = table.index(key) + 1
        return table[(table.index(encrypted_text[0]) - weight)]
    elif len(encrypted_text) == '':
        return ''

    if rotation > 0:
        for i in range(rotation):
            encrypted_text = encrypted_text[1:] + encrypted_text[0]
    elif rotation < 0:
        for i in range(-rotation):
            encrypted_text = encrypted_text[0] + encrypted_text[1:]

    unrotation = encrypted_text
    answer = ''
    for i, k in enumerate(key):
        weight = table.index(k) + 1
        answer += table[(table.index(unrotation[i]) - weight)]

    return answer

# solution('hellopython','abcdefghijk',3)
print(solution('qyyigoptvfb','abcdefghijk',-3))
print(solution("bac", "dbc", 3))
