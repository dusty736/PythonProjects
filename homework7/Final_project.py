import requests
from bs4 import BeautifulSoup
import json

#url = "http://simbad.u-strasbg.fr/simbad/sim-id?Ident=%40593403&Name=NVSS%20J101606%2b470806&submit=submit#lab_meas"
#r = requests.get(url)

#soup = BeautifulSoup(r.content, "html5lib")
#organized = soup.find('spec')
#print organized

#soup = BeautifulSoup(response.content, "html5lib")

#font = soup.find("b", text="Past Movies:").find_next_sibling("font")
##for event in font.find_all("b", recursive=False):
 #  event_date = event.previous_sibling.strip()
 #  event_text = event.get_text(strip=True)
 #  print(event_date, event_text)
 
def read_spectrum_data(filename):
    """
    
    """

    with open(filename) as data_file:    
        data = json.load(data_file)
    return data
    
print read_spectrum_data("dusty3_J1016+4706.json")
    