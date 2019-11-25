

# # STRING COMPARISON ARE CASE SENSITIVE
# country = 'Canada'
# if country.lower() == 'canada':
#     print('Look a canadian!')
# else:
#     print('Not a canadian')


# price = input('How much did you pay? ')
# price = float(price)
# if price >= 1.00:
#     tax = .07
# else:
#     tax = 0
# print(tax)


# # More than one condition
# province = input('Which province are you from? ')
# province = province.lower()
# if province == 'alberta':
#     or province == 'nunavut':
#     tax = 0.05
# elif province == 'ontario':
#     tax = 0.13
# else:
#     tax = 0.15
# print(tax)


# # Multiple Conditions
# country = 'Canada'
# country = country.lower()

# if country == 'canada':
#     if province in ('alberta', 'nunavut', 'yukon'):
#         tax = 0.05
#     elif province == 'ontario':
#         tax = 0.13
#     else:
#         tax = 0.15
# else:
#     tax = 0.0
# print(tax)


# COMPLEX CONDITIONS
gpa = float(input('What was your GPA? '))
lowest_rate = float(input('What is your lowest rate? '))
if gpa >= .85 and lowest_rate >= .70:
    honuor_roll = True
else:
    honuor_roll = False
# Somewhere latter in your code if you need to check if students is on honour roll,
# all I need to do is check the boolean varible I set eilier in my code.
if honuor_roll:
    print('You made the honuor roll!')
