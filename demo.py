

import requests

# Assume you've already obtained an access token
#access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ2eWI4MjAzNi5DT1JURVhTQSIsInN1YiI6IkNPUlRFWFNBIiwiaWF0IjoxNzI3MTYxNTI3LCJleHAiOjE3MjcxNjE1ODd9.LzHQYm4mvpiTeuQybnzXp0myhielT9i50RqwJNAzaioXGXks1-P7Las75XNurXvvl66b67XunID_bjDFXp5JoYsLl8C4HKtibCK2Mv5FSNOFIXRp4Wvtzvx11wfPf6p0pnImJrBL8CTdRQz8Yriq_DFGnkFnhKrTuS097sYQq6hKvTv7rpBqLUhbjrv7_X6Wt1EIxeD-E_RtfShRpR3ElWOc6EPWh8Z9Uu16ZlLxBhXtZ3ebMI0ibzcu8JnzXAC5hTjQPUtVAlQnR57Ayxkp3wtuNBrpVkowFI0FC-D-vWFIV_HGbX3SbTv7WjPY6xz1qZXultoe20AhOcdXFCWD2w"
access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJWWUI4MjAzNi5DT1JURVhTQS5TSEEyNTY6Rk9xRVVtQ1J2SXA3RVR6b0U2MjcwNldhRFZWTk9wVmZVRFRaNTVwYzM1Zz0iLCJzdWIiOiJWWUI4MjAzNi5DT1JURVhTQSIsImlhdCI6MTcyNzE3MTIwMCwiZXhwIjoxNzI3MjU3NjAwfQ.auy1pEQrBT1ky8IQk6-SHLzWXFNDMGg3a9aaXVL1BKbFKfT1uZteRbqDKLsII8SgJqzCFQjW2R5jMQ29HZjAgoVqk05F4bw97BfYPp1uQ3sCVWh39bt2XZsczYcJBPmfs8tnoQj9SfQeAurzhdN7XwXW8hGmz7QowMKGw3AYrO2ZdrYSY18FCY-LJm4MkbvNgOzlvQpVcVRos6glJN8H9lqYnaFi76QJN4GL1yI3GGsljxh9ezgI0c0DaWRND4akT89mY2ctKRhhSdf6d_7ziOBuPjVr4Qhe5gJcMLV-m_14vlyRfJRnzA9agiN7mmSEEv5gKQmrIiAwbpQE-nT_OQ'

# Snowflake account and API endpoint
account = "vyb82036"
api_endpoint = f"https://{account}.snowflakecomputing.com/api/v2/statements"



# SQL statement to call your stored procedure
sql_statement = "CALL cortex_search_procedure('Explain Oncology', 'RELATIVE_PATH', 'Cardiology_Comprehensive_Overview.pdf', 5);"

# Construct the request payload
payload = {
    "statement": sql_statement,
    "timeout": 60,  # timeout in seconds
    "database": "CORTEX_LAB_DB",
    "schema": "CORTEX_LAB_SCHEMA",
    "warehouse": "CORTEX_LAB_WH"
}

# Set up the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}",
    "X-Snowflake-Authorization-Token-Type": "KEYPAIR_JWT"
}

# Send the request
response = requests.post(api_endpoint, json=payload, headers=headers)
print(response)
# Handle the response
if response.status_code == 200:
    result = response.json()
    print("Stored procedure executed successfully:", result)
else:
    print("Error executing stored procedure:", response.text)