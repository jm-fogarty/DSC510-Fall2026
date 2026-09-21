# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Julie Fogarty
# September 17, 2026

# Create and print a welcome message to welcome the customer.
welcome_message= (
    "Welcome! We're happy to help you with all your fiber optic needs."
)
print(welcome_message)
# Gather customer information using inputs.
company_name = input('Please enter the name of your company:')
print(company_name)
# While Loop adapted from Stack Overflow discussion
# Author Joseph, A
# Available at https://stackoverflow.com/questions/43199973/show-an-error-message-to-the-user-if-what-they-entered-is-not-a-float
is_balance_not_float = True
while is_balance_not_float:
    try:
        cable_needed = float(input('Please enter the amount of cable needed, in feet:'))
        print("You entered: ", cable_needed)
    except ValueError:
        print("Please enter only a numeric value")
    else: is_balance_not_float = False
# Calculate the installation cost.
price = 0.95
installation_cost = cable_needed * price
print("Your cost: $", installation_cost)
# Print Receipt.
print('Thank you for your purchase!')
print("--------")
print('Bill to:', company_name)
print('Cable:', cable_needed, '@ $',price,"per foot" )
print('Total Cost: $', "%.2f" %installation_cost)