from datetime import datetime, timedelta

current_date = datetime.now()

birthday = input('When is your birthday (dd/mm/yyyy)? ')
# Converting date string into datetime specifc format
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
# one_day = timedelta(days=1)
# birthday_eve = birthday_date - one_day

# Calc how old they are
current_year = current_date.year
birthday_year = birthday_date.year
year_old = int(birthday_year) - int(current_year)
age = 'You are {} years-old!'.format(year_old)

print('Today is ' + str(current_date))
print('Your birthday is ' + str(birthday_date))
print('Your birthday is ' + str(birthday))
print(age)
