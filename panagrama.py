def panagrama(s):
    abecedario = 'zxcvbnmasdfghjklqwertyuiop'
    status = None
    for i in range(26):
        encontrar = s.lower().find(abecedario[i])
        if encontrar != -1:
            status = "pangram"
        else:
            status = "not pangram"
            break
    return status


s = input('')
print(panagrama(s))
