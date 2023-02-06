# Author:       Your-Name
# ULID/Section: Your-ULID & lecture section-number go here

# Print 2 blank lines
print("")
print("")

# Part I of this lab is using input statements and arithmetic expressions

# Ask the user to input hours and hourly rate
# Complete or correct the following input statements 
hours = eval(input("Enter the hours worked: "))
rate = eval(input("Enter in the rate"))

# Write an equation to compute gross pay using the variables above
# The gross pay calculation is hours multiplied by rate
# The overtime should be ONLY the hours OVER 40 hours * rate * 1.5

grossPay = hours * rate
overtimePay = (hours - 40) * rate * 1.5

# Print 1 blank line in your output 
print("")

# Print out hours, rate, gross pay and overtime pay computed
# See the sample output for a recommendation on how to display items
print("Hours =", hours)
print("Rate = ", rate)
print("Gross pay =", grossPay)
print("Overtime Pay = ", overtimePay)


