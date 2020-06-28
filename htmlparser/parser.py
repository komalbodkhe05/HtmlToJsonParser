import json
from bs4 import BeautifulSoup

with open(r'.\html.html', "r") as f:
    page = f.read();
soup = BeautifulSoup(page, 'html.parser');
name = soup.find(id="name").text;
email = soup.find(id="email").text;
phone = soup.find(id="phone").text;
beds = soup.find(id="beds").text;
baths = soup.find(id="baths").text;
address = soup.find(id="address").text;
data_set = {"name": name, "email": email, "phone": phone, "beds": beds, "address": address}
json_dump = json.dumps(data_set);

with open('output.json', 'w') as outfile:
    json.dump(json_dump, outfile)
