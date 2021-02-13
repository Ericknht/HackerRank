def getSubstringCount(s):
    # Write your code here
    zero = 0
    one = 0
    i_chng = 0
    n_chng = 0
    sub_s = 0
    i = 0
    while i < len(s):
        print(i)
        if s[i] == '0':
            zero += 1
            if one > 0:
                if n_chng == 1:
                    sub_s += min(zero, one)
                    i = i_chng
                    n_chng = 0
                    one = 0
                    zero = 0
                    i_chng = 0
                else:
                    n_chng += 1
                    i_chng = i
                    i += 1
            else:
                i += 1

        elif s[i] == '1':
            one += 1
            if zero > 0:
                if n_chng == 1:
                    sub_s += min(zero, one)
                    i = i_chng
                    n_chng = 0
                    one = 0
                    zero = 0
                    i_chng = 0
                else:
                    n_chng += 1
                    i_chng = i
                    i += 1
            else:
                i += 1

    return sub_s


if __name__ == '__main__':


    s = input()

    result = getSubstringCount(s)

    print(str(result))
