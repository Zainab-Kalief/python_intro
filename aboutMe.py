def about(me):
    sentence = 'My '
    for key,val in me.iteritems():
        print sentence + key + ' is ' + val

about({'name': 'Wura',
        'age': '22',
        'country of birth': 'Nigeria',
        'fav language': 'Swift'})
