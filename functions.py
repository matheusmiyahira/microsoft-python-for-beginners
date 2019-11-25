# import datetime

# # Printing data and time
# def print_time():
#     print('task completed')
#     # I have to repeat datetime twice (library.module.now()) as i didn't import the module in the import statement
#     print(datetime.datetime.now())
#     print()


# # Printing date, time and taskname
# def print_time(task_name):
#     print(task_name + ' - task completed')
#     # I have to repeat datetime twice (library.module.now()) as i didn't import the module in the import statement
#     print(datetime.datetime.now())


# first_name = 'Susan'
# print_time('first name assined')

# for x in range(0, 10):
#     print(x)

# print_time('loop')


# # Extracting name initials
# def extract_initials(name):
#     initials = name[0:1].upper()
#     return initials


# first_name = input('What is your first name? ')
# last_name = input('What is your last name? ')

# print('Your initials are: ' + extract_initials(first_name) +
#       extract_initials(last_name))


# # Functions with multiples parameters
# # Setting default value to parameters makes the parameters optional to be passed
# def extract_initials(name, force_upper=True):
#     if force_upper:
#         initials = name[0:1].upper()
#     else:
#         initials = name[0:1].lower()
#     return initials


# first_name = input('What is your first name? ')
# last_name = input('What is your last name? ')

# print('Your initials are: ' + extract_initials(first_name) +
#       extract_initials(last_name, False))


# Named notation practical example

def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error: ' + error_message)


first_name = 10
second_name = 5

if first_name > second_name:
    #error_logger(45, 1, True, 'Second number greater than first', 'my_math_method')
    error_logger(error_code=45, error_severity=1, log_to_db=True,
                 error_message='Second number greater than first',
                 source_module='my_math_method')
