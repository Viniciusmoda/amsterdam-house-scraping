import re
from bs4 import BeautifulSoup
import requests

def get_soup(url):
    page = requests.get(url).text
    soup = BeautifulSoup(str(page), 'html.parser')
    return soup

def get_item_urls(url):
    soup = get_soup(url)
    links = soup.find_all('a', class_ = 'listing-search-item__link listing-search-item__link--title')
    links = [''.join('https://www.pararius.com' + link['href']) for link in links]
    return links

def get_soup(url):
    page = requests.get(url).text
    soup = BeautifulSoup(str(page), 'html.parser')
    return soup

def get_item_urls(url):
    soup = get_soup(url)
    links = soup.find_all('a', class_ = 'listing-search-item__link listing-search-item__link--title')
    links = [''.join('https://www.pararius.com' + link['href']) for link in links]
    return links

def get_price(soup):
    price = soup.find('dd',class_="listing-features__description listing-features__description--for_rent_price").get_text().split()[0]
    return price

def get_offerd_since(soup):
    offered_since = soup.find('dd' ,class_="listing-features__description listing-features__description--offered_since")
    if offered_since:
        offered_since = offered_since.get_text()
    else:
        offered_since = "Not Avalliable"
    return offered_since

def get_status(soup):
    status = soup.find('dd' ,class_="listing-features__description listing-features__description--status")
    if status:
        status = status.get_text()
    else:
        status = "Not Avalliable"
    return status

def get_acceptance(soup):
    acceptance = soup.find('dd' ,class_="listing-features__description listing-features__description--acceptance")
    if acceptance:
        acceptance = acceptance.get_text()
    else:
        acceptance = "Not Avalliable"
    return acceptance

def get_deposit(soup):
    deposit = soup.find('dd' ,class_="listing-features__description listing-features__description--deposit")
    if deposit: 
        deposit = deposit.get_text()
    else:
        deposit = "Not Avalliable"
    return deposit

def get_interior_descripition(soup):
    interior_descripition = soup.find('dd' ,class_="listing-features__description listing-features__description--interior")
    if interior_descripition: 
        interior_descripition = interior_descripition.get_text()
    else:
        interior_descripition = "Not Avalliable"
    return interior_descripition

def get_upkeep_descripition(soup):
    upkeep_descripition = soup.find('dd' ,class_="listing-features__description listing-features__description--upkeep")
    if upkeep_descripition: 
        upkeep_descripition = upkeep_descripition.get_text()
    else:
        upkeep_descripition = "Not Avalliable"
    return upkeep_descripition

def get_living_area(soup):
    living_area = soup.find('dd' ,class_="listing-features__description listing-features__description--surface_area")
    if living_area: 
        living_area = living_area.get_text()
    else:
        living_area = "Not Avalliable"
    return living_area

def get_address(soup):
    address = soup.find('div' ,class_="listing-detail-summary__location")
    if address: 
        address = address.get_text()
    else:
        address = "Not Avalliable"
    return address

def get_rooms_number(soup):
    rooms_numbers = soup.find('dd' ,class_="listing-features__description listing-features__description--number_of_rooms")
    if rooms_numbers: 
        rooms_numbers = rooms_numbers.get_text()
    else:
        rooms_numbers = "Not Avalliable"
    return rooms_numbers

def get_bedrooms_number(soup):
    bedrooms_numbers = soup.find('dd' ,class_="listing-features__description listing-features__description--number_of_bedrooms")
    if bedrooms_numbers: 
        bedrooms_numbers = bedrooms_numbers.get_text()
    else:
        bedrooms_numbers = "Not Avalliable"
    return bedrooms_numbers

def get_bathrooms_number(soup):
    bathrooms_numbers = soup.find('dd' ,class_="listing-features__description listing-features__description--number_of_bathrooms")
    if bathrooms_numbers: 
        bathrooms_numbers = bathrooms_numbers.get_text()
    else:
        bathrooms_numbers = "Not Avalliable"
    return bathrooms_numbers

def get_facilities(soup):
    facilities = soup.find('dd' ,class_="listing-features__description listing-features__description--facilities")
    if facilities: 
        facilities = facilities.get_text()
    else:
        facilities = "Not Avalliable"
    return facilities

def get_dwelling_type(soup):
    dwelling_type = soup.find('dd' ,class_="listing-features__description listing-features__description--dwelling_type")
    if dwelling_type: 
        dwelling_type = dwelling_type.get_text()
    else:
        dwelling_type = "Not Avalliable"
    return dwelling_type

def get_property_types(soup):
    property_types = soup.find('dd' ,class_="listing-features__description listing-features__description--property_types")
    if property_types: 
        property_types = property_types.get_text()
    else:
        property_types = "Not Avalliable"
    return property_types

def get_construction_type(soup):
    construction_type = soup.find('dd' ,class_="listing-features__description listing-features__description--construction_type")
    if construction_type: 
        construction_type = construction_type.get_text()
    else:
        construction_type = "Not Avalliable"
    return construction_type

def get_construction_period(soup):
    construction_period = soup.find('dd' ,class_="listing-features__description listing-features__description--construction_period")
    if construction_period: 
        construction_period = construction_period.get_text()
    else:
        construction_period = "Not Avalliable"
    return construction_period

def lat_lon_regex(datail_map_div):
    lat_lon_regex = r'<div class="detail-map map" data-controller="detail-map" data-detail-map-latitude="(?P<Lat>\d{0,5}.\d{0,5})" data-detail-map-longitude="(?P<Lon>\d{0,5}.\d{0,5})" data-detail-map-type="listing">'
    lat_lon = re.compile(lat_lon_regex)
    match = lat_lon.match(datail_map_div)
    if match:
        groups = match.groupdict()
        lat = groups['Lat']
        lon = groups['Lon']
        point = f'SRID=4326; Point({lon},{lat})'
    return point

def get_map_point(soup):
    datail_map_div = str(soup.find('div' ,class_="detail-map map"))
    point = lat_lon_regex(datail_map_div)
    return point

def get_transfer_data(soup,url):
    address = get_address(soup)
    price = get_price(soup)
    living_area = get_living_area(soup)
    offerd_since = get_offerd_since(soup)
    status = get_status(soup)
    acceptance = get_acceptance(soup)
    deposit = get_deposit(soup)
    interior_descripition = get_interior_descripition(soup)
    upkeep_descripition = get_upkeep_descripition(soup)
    rooms_number = get_rooms_number(soup)
    bedrooms_number = get_bedrooms_number(soup)
    bathrooms_number = get_bathrooms_number(soup)
    facilities = get_facilities(soup)
    dwelling_type = get_dwelling_type(soup)
    property_types = get_property_types(soup)
    construction_type = get_construction_type(soup)
    construction_period = get_construction_period(soup)
    point = get_map_point(soup)
    
    transfer_data = {
        "url" : url,
        "address" : address,
        "point" : point,
        "price" : price,
        "living_area" : living_area,
        "rooms_number" : rooms_number,
        "bedrooms_number" : bedrooms_number,
        "bathrooms_number" : bathrooms_number,
        "facilities" : facilities,
        "offerd_since" : offerd_since,
        "status" : status,
        "acceptance" : acceptance,
        "deposit" : deposit,
        "interior_descripition" : interior_descripition,
        "upkeep_descripition" : upkeep_descripition,
        "dwelling_type" : dwelling_type,
        "property_types" : property_types,
        "construction_type" : construction_type,
        "construction_period" : construction_period,
        
                    }
    return transfer_data

