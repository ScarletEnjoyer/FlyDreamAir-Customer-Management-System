import os

import pandas as pd
from object.countries import Countries
from object.country import Country
from object.administrativeDivision import AdministrativeDivision
import pickle


def readCountryInfoFast():
    """
    Reads country information from a pre-saved pickle file.

    :return: An instance of the Countries class containing country information.
    """
    with open('countryInfo.pkl', 'rb') as f:
        countries = pickle.load(f)
    return countries


def readCountryInfo():
    """
    Reads country information from a text file and populates the Countries class.

    If the pre-saved pickle file exists, it reads from there; otherwise,
    it loads the data from 'countryInfo.txt' and 'admin1CodesASCII.txt' and
    'admin2Codes.txt' to create a structured representation of countries and
    their administrative divisions. The data is then saved to a pickle file
    for faster future access.

    :return: An instance of the Countries class containing country information.
    """
    if os.path.exists('countryInfo.pkl'):
        return readCountryInfoFast()
    countries = Countries()
    country_info_df = pd.read_csv('countryInfo.txt', delimiter='\t', comment='#')
    admin1_df = pd.read_csv('admin1CodesASCII.txt', delimiter='\t', header=None, names=['code', 'name', 'name_ascii', 'geo'])
    admin1_df[['country_code', 'admin1_code']] = admin1_df['code'].str.split('.', expand=True)
    admin2_df = pd.read_csv('admin2Codes.txt', delimiter='\t', header=None, names=['code', 'name', 'name_ascii', 'geo'])
    admin2_df[['country_code', 'admin1_code', 'admin2_code']] = admin2_df['code'].str.split('.', expand=True)
    for index, row in country_info_df.iterrows():
        country_code, country_name = row['ISO'], row['Country']
        country = Country(country_code, country_name)
        admin1_in_country = admin1_df[admin1_df['country_code'] == country_code]
        for index2, admin1_row in admin1_in_country.iterrows():
            admin1_code, admin1_name = admin1_row['admin1_code'], admin1_row['name']
            admin1 = AdministrativeDivision(admin1_name)
            admin2_in_admin1 = admin2_df[(admin2_df['country_code'] == country_code) & (admin2_df['admin1_code'] == admin1_code)]
            for index3, admin2_row in admin2_in_admin1.iterrows():
                admin2_code, admin2_name = admin2_row['admin2_code'], admin2_row['name']
                admin2 = AdministrativeDivision(admin2_name)
                admin1.add_next_level_division(admin2)
            country.add_administrative_division(admin1)
        countries.add_country(country)
    with open('countryInfo.pkl', 'wb') as f:
        pickle.dump(countries, f)
    return countries

#
# if __name__ == '__main__':
#     readCountryInfo()
