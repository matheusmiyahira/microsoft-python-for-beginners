joe = {}
joe['first'] = 'Joe'
joe['last'] = 'Doe'

susan = {'first': 'Susan', 'last': 'Ibach'}

people = [joe, susan]

people.append({'first': 'Bill', 'last': 'Gates'})

presenters = people[0:2]

print(presenters)
