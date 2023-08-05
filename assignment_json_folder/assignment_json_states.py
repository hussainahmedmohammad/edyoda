# 2. Create a dictionary of any 7 Indian states and 
# their capitals.Write this into a JSON file.

import json
details = {'telangana' : 'Hyderabad',
           'maharastra': 'mumbai',
           'tamilnadu' : 'chennai',
           'karnataka' : 'bengaluru',
           'rajasthan' : 'jaipur',
           'goa' : 'panaji',
           'west bengal': 'kolkata' 
}

with open("states.json",'w') as f:
    json.dump(details, f, indent = 3)