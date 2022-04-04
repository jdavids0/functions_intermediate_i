# 1.
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# # In the sports_directory, change 'Messi' to 'Andres'
# # Change the value 20 in z to 30

x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


def changeValues():
    x[1][0] = 15
    students[0]["last_name"] = "Bryant"
    sports_directory["soccer"][0] = "Andres"
    z[0]["y"] = 30
    print(x)
    print(students)
    print(sports_directory)
    print(z)


changeValues()

# # 2. Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for x in range(len(students)):
        print(students[x].keys())
        print(students[x].values())


iterateDictionary(students)

# # 3. Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary2(x, some_list):
#     for i in range(len(some_list)):
#         print(some_list[i][x])

# iterateDictionary2("first_name", students)
# iterateDictionary2("last_name", students)

# # 4. Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def getInfo(some_dict):
    for x in some_dict:  # for loop to run through dictionary
        # using len () to get length of list,
        print(f'{len(some_dict[x])} {x.upper()}')
        for v in some_dict[x]:
            print(v)


getInfo(dojo)

# 7 LOCATIONS
# all locations

# 8 INSTRUCTORS
# all instructors

# print(some_dict.keys())
# print(some_dict.values())

# def getInfo(some_dict):
#     loc = 0
#     instr = 0
#     for x in range(len(some_dict)):
#         # print(some_dict[x].keys)
#         # for i in range(len([x])):
#         #     loc

# getInfo(dojo)
