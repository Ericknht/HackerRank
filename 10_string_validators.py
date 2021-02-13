if __name__ == '__main__':
    s = input()
    t = [False, False, False, False, False]

    for l in s:
        if l.isalnum(): t[0] = True
        if l.isalpha(): t[1] = True
        if l.isdigit(): t[2] = True
        if l.islower(): t[3] = True
        if l.isupper(): t[4] = True
    print(*t, sep='\n')