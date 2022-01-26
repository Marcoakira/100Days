travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#aTODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(a,b,c):
    travel_log.append({"country": a, "visits": b, "cities": c})



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# travel_log.append( {"country": "Russia", "visits": 2, "cities":["Moscow", "Saint Petersburg"]})
print(travel_log)
#tentativas e erros
#{"country": "Russia", "visits": 2, "cities":["Moscow", "Saint Petersburg"]}

