if __name__ == '__main__':
    n = int(input())
    l = list()

    """
    list_input = []
    for i in range(N):
        list_input = input().split(' ')

        if list_input[0] == 'insert':
            arr.insert(int(list_input[1]), int(list_input[2]))
        elif list_input[0] == 'print':
            print(arr)
        if list_input[0] == 'remove':
            arr.remove(list_input[1])
        elif list_input[0] == 'append':
            arr.append(list_input[1])
        elif list_input[0] == 'sort':
            arr.sort()
        elif list_input[0] == 'pop':
            arr.pop()
        elif list_input[0] == 'reverse':
            arr.reverse()
    """

    for _ in range(n):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print(l)