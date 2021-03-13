
def dif_oddsumcount(n):
    if n == 0:
        return 0
    else:
        odd_numbers = []
        # Gets all the odd numbers
        for i in range(1, n + 1, 2):
            odd_numbers.append(i)

        print(odd_numbers)
        num_odd_numbers = len(odd_numbers)
        sum_odd_numbers = 0
        for num in odd_numbers:
            sum_odd_numbers += num

        return abs(sum_odd_numbers - num_odd_numbers)
