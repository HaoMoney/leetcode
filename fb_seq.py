import sys
def get_fb(num):
    res = [1] * (num+1)
    for i in range(num+1):
        if i < 2:
            res[i] = i
        else:
            res[i] = res[i-1] + res[i-2]
    return res
print(get_fb(3))
