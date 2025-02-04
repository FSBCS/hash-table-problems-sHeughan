def count_subarrays_with_sum(arr, sum):
    correct_sums = 0
    number_of_sums = {}
    sum_c = 0
    current_arr = []
    for x in arr:
        sum_c = 0
        current_arr.append(x)
        for x in current_arr:
            sum_c += x
        
        if sum_c == sum:
            correct_sums += 1
        
        n_sum = sum_c - sum
        print(n_sum)

        if n_sum in number_of_sums:
            if number_of_sums[n_sum] > 0:
                correct_sums += number_of_sums[n_sum]

        if sum_c not in number_of_sums:
            number_of_sums[sum_c] = 1
        
        else:
            number_of_sums.update({sum_c: number_of_sums[sum_c] + 1})
        
        print(number_of_sums)
        
        print(correct_sums)
        print("____")

    return correct_sums
        
            

print(count_subarrays_with_sum([1, -1, 1, 1, 1], 2))