# Write a program to create one string tuple and one numeric tuple.
# 1. Print out the maximum and minimum value from the both.
# 2. Slice the string tuple from the index 2 to 4.

character = ("emeka", "cup", "kettle", "yam","bread")
number = (10,29,40,50,23)
smallchar = min( character)
bigchar = max( character)
print(smallchar, bigchar)

smallnum = min(number)
bignum = max(number)
print(smallnum,bignum)

ind =  character[2:4]
print(ind)


#Problem Statement:
# Write a program to create two dictionary objects named states and cities with the following
# items:
# States :
# Cities
# "Oregon'- "OR'
# 'CA' 'San Francisco'
# "Florida': 'FL'
# 'MI'. 'Detroit
# 'Californi|s!: 'CA'
# 'FL': 'Jacksonville
# "New York': 'NY"
# 'Michigan': 'MI"
# In addition add more two items to the cities dictionary(NY-New York, OR-Portland). Then
# print the details available in cities dictionary using keys and values

states = {
    'oregon' : 'OR',
    'florida': 'FL',
    'Califonia':'CA',
    'New york': 'NY',
    'Michigan': 'MI'
}

Cities = {
    'CA': 'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'

}

Cities['NY'] = 'New York'

Cities['OR'] ='Portland'

print(Cities.keys() , Cities.values())