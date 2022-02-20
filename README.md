#Election Analysis and Audit

## Overview of Project
We must complete additional analysis on data set including numbers and reports on:
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

### Purpose
To analyze election results per county, per candidate, and to break down election votes totals and percentages by population. 

## Results Summary

### Analysis of Votes by County
Jefferson county and Araphahoe county made up just over 17% of the data set. Denver had the highest number of voters by over 80%. This is likely due to its hgih and dense population. 


## Methods
Given the large amount of data present in this data set, it was necessary to perform several manipulations, including:
* Creating and adding to lists
* Creating and adding keys, values to dictionaries
* Use of if statements, while loops, and for loops to iteratively check our lists and dictionaries against chosen parameters
* Use of f-strings to display data in a text file in a logical and readable way
* Output to a text file for delivery

#Election-Audit Results
The results in this audit are as follows:
* Number of votes cast: 369,711
* Number of votes and percentage of total votes for each county:
  * Jefferson: received 10.5% of the votes (38,855)
  * Denver: received 82.8% of the votes (306,055)
  * Arapahoe: received 6.7% of the votes (24,801)
* County with largest number of votes: Denver
* Number of votes and percentage of total votes each candidate received:
  * Charles Casper Stockham: 23.0% (85,213 votes)
  * Diana DeGette: 73.8% (272,892 votes)
  * Raymon Anthony Doane: 3.1% (11,606 votes)
* Winning candidate, vote count, and percentage of total votes: 
  * Diana DeGette, 272,892 votes (73.8% of the total vote)

#Election-Audit Summary
Diana DeGette won the election, netting 73.8% of the votes. It seems as though Denver, with its large population and large voter turnout, will decide elections for much of the state of Colorado. This script can be used for more counties if more counties are added to the list of counties and to the dictionaries. This script can also be modified to use in smaller elections, ie county elections, by changing the dictionaries to store town/city names isntead of counties. The script could further be modified to accept more candidates, or even analyze multiple races at a time, if a new dictionary was added that could sort lists/dictionaries of candidates and their votes into specific electoral races (ie, treasurer, president, vice president, etc). 
