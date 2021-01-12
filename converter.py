arabe_roman_correlation = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

def to_roman_numerals(n):
    resu = ''
    if n != 0:
        sps_1000 = max(arabe_roman_correlation)
        resu += arabe_roman_correlation[sps_1000] * (n // sps_1000)
        n %= sps_1000
    list_used_arabe = list(arabe_roman_correlation)
    list_used_arabe.sort()
    i = len(list_used_arabe) - 1
    big_step = list_used_arabe[1] // list_used_arabe[0]
    while n > 0:
        while list_used_arabe[i - 1] > n:
            i -= 1
        j = i
        if list_used_arabe[i] // list_used_arabe[i-1] < big_step:
            j -= 2
        else:
            j -= 1
        if n >= (list_used_arabe[i] - list_used_arabe[j]):
            resu += arabe_roman_correlation[list_used_arabe[j]]
            resu += arabe_roman_correlation[list_used_arabe[i]]
            n -= list_used_arabe[i] - list_used_arabe[j]
        else:
            resu += arabe_roman_correlation[list_used_arabe[i-1]] \
                 * (n // list_used_arabe[i-1])
            n %= list_used_arabe[i-1]
        i -= 1
    return resu
    

if __name__ == '__main__':
    n = int(input('Enter your number: '))
    print(to_roman_numerals(n))