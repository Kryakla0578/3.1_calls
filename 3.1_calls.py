calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(_string):
    my_tuple = (len(_string), _string.upper(), _string.lower())
    count_calls()
    print(my_tuple)


def is_contains(_string, _list_to_search):
    count_calls()
    if any((match := substring) in _string for substring in _list_to_search):
        print(True)
    else:
        print(False)


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBan'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
