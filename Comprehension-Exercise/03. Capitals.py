countries = input().split(', ')
capitals = input().split(', ')
result = {countries[index]: capitals[index] for index in range(len(countries))}
print(*[f"{countries} -> {capitals}" for countries, capitals in result.items()], sep='\n')