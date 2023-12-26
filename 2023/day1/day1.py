
def check(l):
    a = ["one", "two", "three", "four", "five", "six", "seven",\
            "eight", "nine"]
    s = ""
    for x in l:
        s+=x
        if s in a:
            return (len(s), a.index(s)+1)
    return l


def nums(l):
    for c in range(len(l)):
        x = check(l[c:])
        if type(x)==tuple:
            l = l[:c] + str(x[1]) + l[c+x[0]:]


    n = ""
    for x in l:
        if x.isdigit():
            n+=x
            break
    for x in l[::-1]:
        if x.isdigit():
            n+=x
            break

    return int(n)

total = 0
for l in open("input.txt"):
    total += nums(l)
print(total)
