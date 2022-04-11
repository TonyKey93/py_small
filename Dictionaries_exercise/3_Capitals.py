def capitals():
    countries = input().split(', ')
    capitals = input().split(', ')

    result = dict(zip(countries, capitals))

    for countries, capitals in result.items():
        print(f'{countries} -> {capitals}')


capitals()