def first_combination_pairs(array, target):
    pairs = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if abs(array[i] + array[j]) == target:
                pairing = [array[i], array[j]]
                already_present = False
                for existing_pair in pairs:
                    if existing_pair == pairing:
                        already_present = True
                        break
                if not already_present:
                    pairs.append(pairing)
    return pairs


def merge_sorted_array(array):
    merged_list = []
    for sub_array in array:
        merged_list.extend(sub_array)
    merged_array = sorted(merged_list)
    return merged_array


def double_target_value(target):
    return target * 2


def second_combination_pairs(nums, target):
    combinations = []
    nums.sort()
    backtrack(nums, target, 0, [], combinations)
    return combinations


def backtrack(nums, target, start, current_combination, combinations):
    if target == 0:
        combinations.append(current_combination[:])
        return

    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue

        num = nums[i]
        if num > target:
            break

        current_combination.append(num)
        backtrack(nums, target - num, i + 1, current_combination, combinations)
        current_combination.pop()


# Test case
nums = [1, 3, 2, 2, -4, -6, -2, 8]
target = 4

sum_pairs = first_combination_pairs(nums, target)
print("First Combination for", target, ":", sum_pairs)

merged_array = merge_sorted_array(sum_pairs)
print("Merge Into a single Array:", merged_array)

doubled_target_value = double_target_value(target)
print(doubled_target_value)

combinations = second_combination_pairs(nums, doubled_target_value)
print("Second Combination for", doubled_target_value, ":", combinations)