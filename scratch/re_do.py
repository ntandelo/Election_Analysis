print("HI")
counties = ["Arapahoe","Denver","Jefferson"]
#print(counties[1:2])
counties.append("El Paso") 
counties.insert(2,"Mickey")
#removes 5th item in list (item 4)
counties.pop(4) 


voting_data=[]

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#print(voting_data)
# print(len(voting_data))

voting_data.insert(2,{"county":"El Paso", "registered_voters": 461149})
voting_data.pop(0)
voting_data[2],voting_data[1] = voting_data[1],voting_data[2]

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#print(voting_data)


#print each dictionary in a list of dictionary
for county_dict in voting_data:
    print(county_dict)

# #get only the counties in the list of dictionaries 
# for i in range(len(voting_data)):
#     print(voting_data[i]['county'])


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)



new_counties = ["Arapahoe","Denver","Jefferson"]

# What is the score?
# score = int(input("What is your test score? "))

# Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')


# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# #get keys
# for county in counties_dict.keys(): 
#     print(county)

# #get values
# for county in counties_dict.values():
#     print(county)

# #get key/value pairs
# for county,voters in counties_dict.items():
#     print(county,voters)