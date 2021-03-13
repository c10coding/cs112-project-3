# -------------------------------------------------------------------------------
# Name: Caleb Owens
# G#: G01210280
# Project 3
# Due Date: 3/14/2021
# -------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
# -------------------------------------------------------------------------------
# References: Lots of StackOverflow
# -------------------------------------------------------------------------------
# Comments and assumptions: N/A
# -------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
# -------------------------------------------------------------------------------

def dif_fibcumsum(n):

    sum_natural_numbers = 0

    fib1 = 0
    fib2 = 1

    # Finds the fib and the sum
    for i in range(n):
        fibn = fib1 + fib2
        fib1 = fib2
        fib2 = fibn
        sum_natural_numbers += n
        n -= 1

    return abs(fib1 - sum_natural_numbers)

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
    # If any of the strings in promotions match cake, then it returns True. If the for loop does it's thing and doesn't return True, it just returns false afterwards.
    for str in promotions:
        if cake == str:
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


def marble_cakes(flavor, flavor_cakes):
    valid_flavor_cakes = flavor_cakes
    should_add_flavor = True
    # If flavor_cakes doesn't have flavor, then it adds it to the valid list so that I can just deal with 1 list instead of a list and a separate entity
    for currentFlavor in flavor_cakes:
        if currentFlavor == flavor:
            should_add_flavor = False

    if should_add_flavor:
        valid_flavor_cakes.append(flavor)

    num_combinations = 0
    for i in range(len(valid_flavor_cakes)):
        valid_flavor_cakes.pop()
        num_combinations += len(valid_flavor_cakes)
    return num_combinations


def get_cakewithtopping(cake, toppings):
    combinations = []
    if len(toppings) == 0:
        return combinations
    else:
        for topping in toppings:
            combination = cake + "-" + topping
            should_add_combination = True
            # If the combination is in the list of combinations, then it won't get added because it's a duplicate
            for comb in combinations:
                if combination == comb:
                    should_add_combination = False
            if should_add_combination:
                combinations.append(cake + "-" + topping)

    return combinations


def sales_sort(cakes, sales):
    if len(cakes) == 0 or len(sales) == 0:
        return []
    else:
        for i in range(len(sales)):
            for x in range(i + 1, len(sales), 1):
                tmp = 0
                tmp2 = ""
                if sales[i] < sales[x]:
                    tmp = sales[i]
                    tmp2 = cakes[i]
                    sales[i] = sales[x]
                    cakes[i] = cakes[x]
                    sales[x] = tmp
                    cakes[x] = tmp2

    return cakes


def dif_sales(cakes, sales):
    dif_list = []
    appearance_count = 1
    for i in range(len(sales)):
        for x in range(len(sales)):
            if i != x:
                if sales[i] == sales[x]:
                    appearance_count += 1
        if appearance_count == 1:
            dif_list.append(cakes[i])
        else:
            appearance_count = 1
    return dif_list
