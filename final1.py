import feedparser
from pprint import pprint 
from datetime import datetime

def get_fuel(product_id, region_name, date):
    data = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Region='+str(region_name)+'&Day='+str(date))
    #not clear whats happen this  str(product_id)
    #pprint(data)
    if date == "today":
        for x in data['entries']:
            x['DATEC']=1

    if date == "tomorrow":
        for x in data['entries']:
            x['DATEC']=2
 

    #pprint(data['entries'])
    return data['entries']
  
def get_fuel_region():

    # learn hoe to up try catch error handaleing

    Tod_data = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=25&Day') 
    Tod_data1 = Tod_data['entries']
    #still dosent understand how it works
    for y in Tod_data1:
     y['TOD'] = 1

    Tom_data = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=25&Day=tomorrow') 
    Tom_data1 = Tom_data['entries']

    for x in Tom_data1:
     x['TOD'] = 2

    Today_and_Tommorow = Tod_data1+ Tom_data1

    #pprint(Today_and_Tommorow)

    return Today_and_Tommorow

def Product_Type(product_id, region_name, date):

    #unleaded = 1
    #premium_unleaded = 2
    #region_name= 25
    #date="today"
    #print('inside')
    #u_prices = get_fuel(unleaded,region_name)
    #pu_prices = get_fuel(premium_unleaded,region_name, date)

    pu_prices = get_fuel(product_id,region_name, date)
    pu_prices_to = get_fuel(product_id,region_name, date)

    for y in pu_prices:
     y['TOD'] = 1

    for x in pu_prices_to:
     x['TOD'] = 2

    Today_and_Tommorow = pu_prices_to + pu_prices

    #pprint(Today_and_Tommorow)
    #Today_and_Tommorow = get_fuel_region()

    my_people=[]
    A_Tod_list=[]

    #price1=0

    for d in Today_and_Tommorow:
        A_Tod_list = {'TOD': d['TOD'],'Price': float(d['price']), 'Brand': d['brand'],'Address': d['address'],'Date': d['date'], 'Phone': d['phone'], 'Location': d['location'], 'Latitude': d['latitude'], 'Longitude' : d['longitude']} 
        my_people.append(A_Tod_list)
        #price1=A_Tod_list['Price']
        #print(type(price1))
    return my_people 

def sort_fun(item):
    return item['Price']


def main_fun(product_id, region_name, date):

    sorted_l1 = sorted(Product_Type(product_id,region_name,date), key=sort_fun)
    #pprint(sorted_l1)


    #pprint(Product_Type())

    #htmllist= sorted_l1

    #pprint(htmllist)

    my_list=''

    l=sorted_l1
    #pprint(l)


    #print(time)

    for x in l:
        price = x['Price']
        address=x['Address']
        brand = x['Brand']
        date = x['Date']
        location=x['Location']
        TOD = x['TOD']

        if TOD==1:
         my_list += '<tr style="background-color:#CC9999" > <td>{price}</td>  <td>{address}</td>  <td>{brand}</td>  <td>{date}</td>  <td>{location}</td></tr>'.format(price=price, address=address, brand=brand, date=date, location=location)

        if TOD==2:
         my_list += '<tr style="background-color:#9999CC"> <td>{price}</td>  <td>{address}</td>  <td>{brand}</td>  <td>{date}</td>  <td>{location}</td></tr>'.format(price=price, address=address, brand=brand, date=date, location=location)

    return my_list

todaydate=(datetime.date(datetime.now()))
date=datetime.now()

