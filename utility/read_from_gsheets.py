import collections
import json

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


# write a python utility to read an excel and create the DDL and DML from the table headers and data.
# This is the sheet link :  https://docs.google.com/spreadsheets/d/1-7Q33eBebr9M3e2JMoJ_r1KK6GMUncMG95W7Skafixo/edit?pli=1#gid=96827606  This is the tab/sheet name : Query_creation_utility.
# Cell Column B1 has the table name. Cell B2-U2 are the column names (which can be extended) Cell B3-U3 to B7-U7 are the data (which can be extended both horizontally and vertically).


#5.1.1 install gspread version this
# Use the credentials file you downloaded from the Google Cloud Console
def read_from_gsheets():
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/hardikgoel/PycharmProjects/Custom_ingestion_LLM'
                                                             '/config/google_creds.json', scope)
    client = gspread.authorize(creds)

    # Open the Google Sheets file
    sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1-7Q33eBebr9M3e2JMoJ_r1KK6GMUncMG95W7Skafixo/edit'
                               '?pli=1#gid=96827606')

    # Select the correct worksheet
    worksheet = sheet.worksheet('Query_creation_utility')

    # Get the headers from the second row (index starts from 1)
    expected_headers = worksheet.row_values(2)

    expected_headers = [header.strip().replace(' ', '_').lower() for header in expected_headers]
    print ("expected_headers::", expected_headers)
    # Get all values from the worksheet
    list_of_hashes = worksheet.get_values()
    print ("list_of_hashes::", list_of_hashes)
    table_name = list_of_hashes[0][0]
    # Convert the list of dictionaries to a list of OrderedDicts
    list_of_ordered_dicts = [collections.OrderedDict(zip(expected_headers, values)) for values in list_of_hashes]
    table_values = list_of_hashes[2:]
    # Convert the list of OrderedDicts to a pandas DataFrame
    df = pd.DataFrame(list_of_ordered_dicts)
    # Create a JSON document
    document = json.dumps([dict(row) for row in list_of_ordered_dicts], indent=4)
    print("Document:", document)
    return df, expected_headers, table_name, table_values, document
