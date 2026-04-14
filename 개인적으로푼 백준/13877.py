for i in range(0, int(input())):
    tc, tn = input().split()
    if '8' in tn or '9' in tn:
        octn = int(0)
    else:
        octn = int(tn, 8)
    print(tc, octn, int(tn, 10), int(tn, 16))