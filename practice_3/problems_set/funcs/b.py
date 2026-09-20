#6
def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)



#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True

    return False


#8
def spy_game(nums):
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1

        if zero_count == 2 and num == 7:
            return True

    return False


#9
def volume(radius):
    return (4 / 3) * 3.14 * radius ** 3


print(volume(5))

#10
def unique_list(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result


print(unique_list([1, 2, 2, 3, 1]))