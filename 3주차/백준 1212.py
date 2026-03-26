ref = ["000", "001", "010", "011", "100", "101", "110", "111"]
result = []
origin = list(input().strip())

for i in range(len(origin)):
    result.append(ref[int(origin[i])])

bboba = "".join(result).lstrip("0")

if bboba == "":
    print("0")
else:
    print(bboba)