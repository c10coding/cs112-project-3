def dif_oddsumcount(n):
    if n == 0:
        return 0
    else:
        odd_numbers = []
        # Gets all the odd numbers
        for i in range(1, n + 1, 2):
            odd_numbers.append(i)

        num_odd_numbers = len(odd_numbers)
        sum_odd_numbers = 0
        for num in odd_numbers:
            sum_odd_numbers += num

        return abs(sum_odd_numbers - num_odd_numbers)


def is_promotion(cake, promotions):
    for str in promotions:
        if (cake == str):
            return True
    return False


def biggest_sale(cakes, sales, flavor_cakes):
    if len(cakes) == 0 or len(sales) == 0:
        return None
    else:

        # Gets the highest sale
        highest_sale = 0
        index_highest_sale = 0
        for i in range(len(sales)):
            sale = sales[i]
            if highest_sale < sale:
                highest_sale = sale
                index_highest_sale = i

        most_sold_cake = cakes[index_highest_sale]
        # Now that we have the most sold cake, we check to see if flavor_cakes has it.
        # If it doesn't have it, the loop essentially does nothing and just returns marble afterwards.
        for flavor in flavor_cakes:
            if most_sold_cake == flavor:
                return "single"

        return "marble"
