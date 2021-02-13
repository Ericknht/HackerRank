def print_rangoli(size):
    # your code goes here
    alphabet = list(map(chr, range(97, 123)))
    my_alphabet = alphabet[:size]

    spaces = (size - 1) * 4 + 1
    lines = list()
    half = spaces // 2
    for idx, letter in enumerate(my_alphabet):
        my_line = ['-'] * spaces
        for n in range(0, size - idx):
            my_line[half - 2 * n] = my_alphabet[idx + n]
            my_line[half + 2 * n] = my_alphabet[idx + n]

        lines.append(my_line)

    for line in lines[::-1]:
        print(*line, sep='')
    for line in lines[1:]:
        print(*line, sep='')


def print_rangoli2(size):
    print("****+Rangoli 2***********+")
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]

    for i in range(size-1, -size, -1):
        x = abs(i)
        if x >= 0:
            line = myStr[size:x:-1] + myStr[x:size]
            print ("--"*x+ '-'.join(line)+"--"*x)


def print_rangoli3(size):
    print("****+Rangoli 3***********+")
    import string
    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(L[:0:-1]+L))




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    print_rangoli2(n)
    print_rangoli3(n)