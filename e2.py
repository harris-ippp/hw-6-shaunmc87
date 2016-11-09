import requests

address="http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

for line in open("ELECTION_ID"): # Loop over each row in the election id file created in q1
  election_lists=line.split() #generates a new variable to spilt each line in the 'election_id'
  #print(election_lists) #Check
  election_year=election_lists[1] # Create a new variable equal to the year element in each of the elections
  #print(election_year) # Check
  address_list=address.format(election_lists[0]) # generates a list of the urls containing the election data by inserting the
  # id numbers from the election list into address variable
  #print(address_list) #check
  resp = requests.get(address_list)
  file_name = "election year_" + election_year + ".csv" # generate a variable to name and set the type of the files to download
  with open(file_name, "w") as out: # creates file to write data to
    out.write(resp.text) # writes data for each election to each file which has been created
