#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.county import County

fs = FileStorage()

# All Counties
all_counties = fs.all(County)
print("All Counties: {}".format(len(all_counties.keys())))
for county_key in all_counties.keys():
    print(all_counties[county_key])

# Create a new County
new_county = County()
new_county.name = "Mandera"
fs.new(new_county)
fs.save()
print("New County: {}".format(new_county))

# All Counties
all_counties = fs.all(County)
print("All Counties: {}".format(len(all_counties.keys())))
for county_key in all_counties.keys():
    print(all_counties[county_key])

# Create another County
another_county = County()
another_county.name = "Turkana"
fs.new(another_county)
fs.save()
print("Another County: {}".format(another_county))

# All Counties
all_counties = fs.all(County)
print("All Counties: {}".format(len(all_counties.keys())))
for county_key in all_counties.keys():
    print(all_counties[county_key])        

# Delete the new County
fs.delete(new_county)

# All Counties
all_counties = fs.all(County)
print("All Counties: {}".format(len(all_counties.keys())))
for county_key in all_counties.keys():
    print(all_counties[county_key])