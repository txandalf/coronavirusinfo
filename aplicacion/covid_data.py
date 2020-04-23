import requests
import json

url = "https://covid-19-data.p.rapidapi.com/report/country/name"

def getResponseJson(country):
    querystring = {"date-format":"YYYY-MM-DD","format":"json","date":"2020-04-23","name":country}
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "c7e5a3b9f2mshc9af553d57c05c9p16369bjsnef8ad3b4bcfd"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    object = json.loads(response.text)
    return object


def getCountryList():
    querystring = {"format":"json"}
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "c7e5a3b9f2mshc9af553d57c05c9p16369bjsnef8ad3b4bcfd"
        }
    urlCountries = "https://covid-19-data.p.rapidapi.com/help/countries"
    response = requests.request("GET", urlCountries, headers=headers, params=querystring)
    object = json.loads(response.text)
    return object


def getCountryInfo(country):
    '''
        La tupla contiene el orden:
        0 -> casos confirmados,
        1 -> recuperados,
        2 -> muertes,
        3 -> casos activos
    '''
    data = getResponseJson(country)
    data = data[0]["provinces"][0]
    info = (data["confirmed"], data["recovered"], data["deaths"], data["active"])
    return info



#data = getCountryInfo("Spain")
#print("\nCasos confirmados: " + str(data[0]))
#print("\nrecuperados: " + str(data[1]))
#print("\nCasos de muerte: " + str(data[2]))
#print("\nCasos activos: " + str(data[3]))
