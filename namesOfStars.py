def dicIn(list):
    for value in list:
        name = ''
        for val in value.itervalues():
            name += val + ' '
        print name

dicIn([
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ])
