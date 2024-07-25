def count_substring(string, sub_string):
    ml = len(string)
    sl = len(sub_string)
    count = 0
    for i in range(ml-sl+1):
        if string[i:i+sl] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

