# You are a cook in a busy restaurant. You are writing a program to help you organize how much of each kind of food you need to cook. Naturally, you decide to take a break from cooking and write a function to help. You decide that your function will take a dictionary as a parameter where the keys are the tables in the restaurant and the values are lists of strings describing the food each table has ordered. Your function returns a dictionary with the totals for how many of each food item you need to cook.



# For example, say you have 5 tables and 3 dishes:

# Tables: t1, t2, t3, t4 and t5

# Dishes: Vegetarian stew, Steak pie, Poutine



# Input:

# You will use the table names as the keys, and use a list of the foods ordered at each table as values.



# For example your dictionary may look like this:

# {'t1': ['Vegetarian stew', 'Poutine', 'Vegetarian stew'],
#  't3': ['Steak pie', 'Poutine', 'Vegetarian stew'],
#  't4': ['Steak pie', 'Steak pie']}


# Output:

# Your function must return a dictionary with the dish as the key, and the number of times that dish was ordered as the value. Given the above input, your function would create and return a dictionary equivalent to the following:

# {'Vegetarian stew': 3, 'Poutine': 2, 'Steak pie': 3}

from typing import List, Dict

def get_quantities(table_to_foods: Dict[str, List[str]]) -> Dict[str, int]:
    # """The table_to_foods dict has table names as keys (e.g., 't1', 't2', and
    # so on) and each value is a list of foods ordered for that table.

    # Return a dictionary where each key is a food from table_to_foods and each
    # value is the quantity of that food that was ordered.

    # >>> get_quantities({'t1': ['Vegetarian stew', 'Poutine', 'Vegetarian stew'],
    # 't3': ['Steak pie', 'Poutine', 'Vegetarian stew'], 't4': ['Steak pie', 'Steak pie']})
    # {'Vegetarian stew': 3, 'Poutine': 2, 'Steak pie': 3}
    # """

    food_to_quantity = {}

    # Accumulate the food information here.

    return food_to_quantity