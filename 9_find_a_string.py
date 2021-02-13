def count_substring(string, sub_string):
    count = 0
    l_ss = len(sub_string)
    l_s = len(string)
    for i in range (0, l_s - l_ss + 1):
        if string[i: i + l_ss].find(sub_string) != -1:
            count += 1
            i = i + l_ss

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)