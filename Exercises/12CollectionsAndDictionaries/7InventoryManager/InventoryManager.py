# ===================== LEVEL: HARD =====================
# TASK 7: Inventory Manager (nested dictionaries)
#
# What to do:
#   Store a shop inventory as a dictionary of dictionaries:
#       inventory = {
#           "laptop": {"price": 1200.0, "quantity": 5},
#           "mouse":  {"price": 25.5,   "quantity": 40},
#           "phone":  {"price": 800.0,  "quantity": 0},
#       }
#
#   Write these functions (each one must be a separate function):
#     1. add_product(inventory, name, price, quantity)
#           - if the product exists, only increase its quantity
#     2. sell_product(inventory, name, amount)
#           - return the total price of the sale
#           - if the product does not exist or the stock is not enough,
#             print a message and return 0
#     3. total_value(inventory)
#           - return the total value of the stock (price * quantity of all)
#     4. out_of_stock(inventory)
#           - return a list of product names with quantity 0
#     5. print_report(inventory)
#           - print a table sorted by product name:
#               laptop.......... 1200.00$ x 5
#
#   Then write a menu (while loop) that lets the user use all these functions.
#
# Bonus: Validate the input (price and quantity must be positive numbers).
#
# Concepts: nested dict, functions, return values, list comprehension, validation

# Write your code below:
