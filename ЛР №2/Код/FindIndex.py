def find_index(nums, target):
    for i in range(len(nums)):
        try:
            j = nums[i + 1:].index(target - nums[i]) + i    # Находим второй элемент пары
            return [i, j + 1]
        except:
            continue
    return -1   # Если пара не найдется, возвращаем -1  