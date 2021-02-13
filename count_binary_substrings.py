def getSubstringCount(s):
    # Write your code here
    num = None
    chng = list()
    # Save all indexes when there is a number change.
    # Ex. 01: change 0 to 1 in index 1, save index 1 in chng list.
    for i in range(0, len(s)):
        if i == 0:
            num = s[i]
        else:
            if s[i] != num:
                chng.append(i)
                num = s[i]

    # count the substrings
    count = 0
    for i in chng:
        count += 1
        for j in range(1,len(s)):
            if i + j < len(s) and i - j > 0:
                if s[i - j - 1] == s[i - 1] and s[i + j] == s[i]:
                    count += 1
    return count



if __name__ == '__main__':


    s = input()

    result = getSubstringCount(s)

    print(str(result))
