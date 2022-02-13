#x = 2
#while x<=5:
    #print(x)
    #x=x+.1
#counties = ['Arapahoe', 'Denver', 'Jefferson']
# for county in counties:
#     print(county)

# for num in range(5):
#     print(num)

# n = len(counties)
# for i in range(len(counties)):
#     print(counties[n-i-1],i)

counties_dict = {"Denver": 463353, "Arapahoe": 422829, "Jefferson": 432438}
# for county in counties_dict.keys():
#     print(county,counties_dict[county]) #have key, looking up in dictionary by key
# print(counties_dict["Denver"])


# key = counties_dict.keys

for county in counties_dict:
      print(county, counties_dict[county])

# for county, voters in counties_dict.items():
#      print(county, "has", voters, "regisetered voters")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# # for county_dict in voting_data:
# #     print(county_dict)

# # for i in range(len(voting_data)):
# #     print(voting_data[i]['county'])

# # for county_dict in voting_data:
# #     for value in county_dict.values():
# #         print(value)

# # my_votes = int(input("How many votes did you get in the election? "))
# # total_votes = int(input("What is the total votes in the election? "))
# # percentage_votes = (my_votes / total_votes) * 100
# # print("I received " + str(percentage_votes)+"% of the total votes.")

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, registered_voters in counties_dict.items():
#     print(f"{county} has {registered_voters:,} registered voters")
