# UNIBIT-ASSIGNMENT
### Here's the step-by-step execution of the code:

* Define the first_combination_pairs function that takes an array and a target value as input.
* Initialize an empty list pairs to store the pairs that satisfy the target condition.
* Iterate over the elements in the array using the outer loop variable i.
* Nested within the outer loop, iterate over the elements from i+1 to the end of the array using the inner loop variable j.
* Check if the absolute sum of array[i] and array[j] equals the target value.
* If the condition is satisfied, create a pairing list [array[i], array[j]].
* Check if the pairing already exists in the pairs list.
* If not, append the pairing to the pairs list.
* Return the pairs list.
  
The ```first_combination_pairs``` function finds all possible pairs from the given array that sum up to the target value.

* Define the merge_sorted_array function that takes an array of pairs as input.
* Initialize an empty list merged_list to store the merged pairs.
* Iterate over the sub-arrays in the input array.
* Extend the merged_list by adding all the elements from each sub-array.
* Sort the merged_list in ascending order.
* Return the sorted merged_list.
  
The ```merge_sorted_array``` function merges the pairs into a single sorted array.

* Define the double_target_value function that takes a target value as input.
* Multiply the target value by 2.
* Return the doubled target value.
* The double_target_value function doubles the target value.

Define the ```second_combination_pairs``` function that takes the array nums and a target value as input.

* Initialize an empty list of combinations to store the combinations.
* Sort the nums array in ascending order.
* Call the backtrack function to find all possible combinations that sum up to the target value.
* Return the combinations list.
  
The ```second_combination_pairs``` function finds all possible combinations from the merged and sorted array.

* Define the backtrack function that takes the array nums, target value, start index, current combination, and combinations list as input.
* Check if the target value is zero. If so, add a copy of the current combination to the combinations list and return.
* Iterate over the elements in the nums array starting from the start index.
* Skip duplicates by checking if the current element is the same as the previous element.
* Check if the current element is greater than the target value. If so, break out of the loop.
* Add the current element to the current_combination.
* Recursively call the backtrack function with the updated target value (target - num), the next index (i + 1), the current combination, and the combinations list.
* Remove the last element from the current_combination to backtrack and try other combinations.
  
The ```backtrack``` function generates all possible combinations using a backtracking algorithm.

* Define the nums array and the target value for the test case.
* Call the first_combination_pairs function with the nums array and target value to find the first combination pairs.
* Print the result of the first combination pairs.
* Call the merge_sorted_array function with the first combination pairs to merge them into a single sorted array.
* Print the merged array.
* Call the double_target_value function with the target value to get the doubled target value.
* Print the doubled target value.
* Call the second_combination_pairs function with the nums array and doubled target value to find the second combination pairs.
* Print the result of the second combination pairs.
