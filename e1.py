import requests
from bs4 import BeautifulSoup

addr =  "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
resp = requests.get(addr)
html = resp.content
soup = BeautifulSoup(html, 'html.parser')

with open("ELECTION_ID", "w") as out:# Generate empty output file
    for result in soup.find_all("tr", "election_item"): #Loop of the elements in the defined address and
     #return all that contian 'election_item' in a table row. Example row: <tr class="election_item general_party" id="election-id-39050">
        id_number = result["id"].split("-")[2] #generate a new variable 'id_number', by searching for "id" in the element (result) and
        #then split this string by the dashes and take the text in the thrid position [2] (ie election-id-44930 == 44930)
        year = result.find("td", "year first").contents[0] #generate a new variable 'year', by searhing within each row an
        # finding the cell titled 'year first' and then return the content of each cell, which is the election year
        out.write("{} {}\n".format(id_number, year)) #print election id_number and year to the "election_id" file
