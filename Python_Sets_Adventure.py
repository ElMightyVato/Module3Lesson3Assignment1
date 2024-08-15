# Task 1: Flight Route Comparison 
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. 
# Write a Python program to find out:

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.

# Example Code:

# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#1.
shared_destinations = our_routes.intersection(competitor_routes) # I'm using intersection to view what they share in common
print(f"These are the routes we share with them: {shared_destinations}")

#2.Unique destinations to our route
our_unique_routes = our_routes.difference(competitor_routes) # I'm using difference to only pull variables that are not in our competitors routes
print(f"These are our routes that our competitor doesn't have: {our_unique_routes}")

#3. Destinations that either airline shares
not_shared = our_routes.symmetric_difference(competitor_routes)
print(f"These are the routes we don't share with each other: {not_shared}")