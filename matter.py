import requests
import os

##############################################################################

headers = {'x-windy-key':'929n1uwLU4gFGkV53IpjWN3vKb8fYfm3'}

##############################################################################

print('''
[1] Get Webcams of Continent
[2] Get Webcams near you
[3] Get Webcam of Country
[4] Help / How to USE??

''')

usr_inp_cat = int(input("$--> "))

##################################################################################

if usr_inp_cat == 1:
    print('''
    Select any One

    [1] EUROPE
    [2] ASIA
    [3] AFRICA

    ''')

    usr_inp_cat_con = int(input("$-- SELECT CONTINENT NUMBER --> "))

    if usr_inp_cat_con == 1:
        api_con = 'https://api.windy.com/api/webcams/v2/list/continent=EU?show=webcams:url'
        response_con = requests.get(url=api_con, headers=headers)
        print(response_con.json())

    elif usr_inp_cat_con == 2:
        api_con = 'https://api.windy.com/api/webcams/v2/list/continent=AS?show=webcams:url'
        response_con = requests.get(url=api_con, headers=headers)
        print(response_con.json())

    elif usr_inp_cat_con == 3:
        api_con = 'https://api.windy.com/api/webcams/v2/list/continent=AF?show=webcams:url'
        response_con = requests.get(url=api_con, headers=headers)
        print(response_con.json())

    else:
        print('no such option found...')

##############################################################################################

elif usr_inp_cat == 2:

    usr_inp_cat_near_lat = float(input(">> Enter your Latitude: "))
    usr_inp_cat_near_lng = float(input(">> Enter You Longitude: "))
    usr_inp_cat_near_rad = int(input('>> Enter Amount of Radius ( Min: 5 & Max: 250 ): '))

    api_near = "https://api.windy.com/api/webcams/v2/list/nearby="+usr_inp_cat_near_lat+','+usr_inp_cat_near_lng+','+usr_inp_cat_near_rad+'?show=webcams:url'

    response_near = requests.get(url=api_near, headers=headers)
    print(response_near.json())

################################################################################################

elif usr_inp_cat == 3:
    print('''
    Select any One

    [1] India
    [2] USA
    [3] Germany

    <-We Are working on adding more countries to our package-> <-Sorry for Inconvinience-> 

    ''')

    usr_inp_cat_coun = int(input("$-- SELECT COUNTRY NUMBER --> "))

    if usr_inp_cat_coun == 1:
        api_coun = 'https://api.windy.com/api/webcams/v2/list/country=IND?show=webcams:url'
        response_coun = requests.get(url=api_coun, headers=headers)
        print(response_coun.json())

    elif usr_inp_cat_coun == 2:
        api_coun = 'https://api.windy.com/api/webcams/v2/list/country=US?show=webcams:url'
        response_coun = requests.get(url=api_coun, headers=headers)
        print(response_coun.json())

    elif usr_inp_cat_coun == 3:
        api_coun = 'https://api.windy.com/api/webcams/v2/list/country=DE?show=webcams:url'
        response_coun = requests.get(url=api_coun, headers=headers)
        print(response_coun.json())

    else:
        print('no such option found...')

elif usr_inp_cat == 4: 
    os.startfile("C:\Aarush Folder\Dev Stuff\Python\Hacking Tools\webmatter\howtouse.txt")