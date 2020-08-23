#예제 1
cities = ["Tokyo", "Shanghai", "Jakarta", "Seoul", "Guangzhou", "Beijing", "Karachi", "Shenzhen", "Delhi" ]

def selected_cities(x):
    selected = [x[i] for i in range(len(x)) if x[i][0] == 'S']
    return selected

print(selected_cities(cities))

#예제 2 
cities  =  [
            ('Tokyo', 36923000), 
            ('Shanghai', 34000000), 
            ('Jakarta', 30000000), 
            ('Seoul', 25514000), 
            ('Guangzhou', 25000000), 
            ('Beijing', 24900000), 
            ('Karachi', 24300000), 
            ('Shenzhen', 23300000), 
            ('Delhi', 21753486)
            ]

def population_of_cities(x):
    dict_cities = { x[i][0]:x[i][1] for i in range(len(x))}
    return dict_cities

print(population_of_cities(cities))

#좋은 답안
cities_dict = {key: value for key, value in cities}
print(cities_dict)