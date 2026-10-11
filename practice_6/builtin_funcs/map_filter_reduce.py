from functools import reduce
nums = [1,2,3,4,5,6,7,8]
print(list(map(lambda x: x*x, nums)))
print(list(filter(lambda x: x>3, nums)))
print(list(map(int, ['1','2','3'])))

print(reduce(lambda acc, x:acc+x, nums))
print(reduce(lambda acc, x: acc+x, [1,2,3,4], 10))