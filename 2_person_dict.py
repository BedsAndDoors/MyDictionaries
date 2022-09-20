from itertools import permutations


person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)
#print(person['children'])
#print(type(person['children']))

#print(person['children'][1])
#print(person['pets'])
#print(person['pets'].get('cat'))
#or
#print(person['pets']['dog'])

for child in person['children']:
    print(child)

for pet in person['pets']:
    print(person['pets'][pet])

