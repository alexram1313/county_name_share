from collections import defaultdict

counties_name_share = set()
num_counties = 0
len_seat_name_share = 0

with open('genealog.uscount1.txt', 'r') as f:
    count = False
    for line in f:
        if count:
            county_name = line[7:33].rstrip()
            if not county_name.endswith("(CITY)"):
                num_counties += 1
                county_seat = line[33:59].rstrip()
                state = line[1:3]
                if county_name == county_seat:
                    counties_name_share.add((county_name,state))
                    len_seat_name_share += 1
        else:
            count = True

def print_county_name_shares():
    print ("These are the following counties or county-equivalents whose names",
           "are shared with their respective county seats...")
    print ()
    for county in counties_name_share:
        print ("  -" + county[0]+",", county[1])

    print (len_seat_name_share, "of the", num_counties, "U.S. Counties",
           "share names.")
    print (str((len_seat_name_share/num_counties)*100) + "%")

def get_num_shares_by_state():
    state_counts = defaultdict(int)
    for county in counties_name_share:
        state_counts[county[1]] += 1
    return state_counts

def print_num_shares_by_state():
    state_counts = get_num_shares_by_state()
    print ("This is the number of county name shares by state.")
    print ("***States not listed have 0***")
    print ()
    for kvp in state_counts.items():
        print ("  -", kvp[0] +":", kvp[1])

def get_shares_in_state(state):
    return {x for x in counties_name_share if x[1]==state}

def print_shares_in_state(state):
    print ("These are the county name shares in", state)
    for county in counties_name_share:
        if county[1] == state:
            print ("  -", county[0] +",", county[1])
