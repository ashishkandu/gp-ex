from functions import *
from mysession import Mysession
from dotenv import load_dotenv
import variables as v
import os

load_dotenv()
my_id = os.getenv('USER_NAME')
my_password = os.getenv('PASSWORD')
store_token = os.getenv('TOKEN')

def run():
    prompt() # A prompt for confirmation of variables set
    session = Mysession() # Create a session

    session.update_parameter({'Authorization': add_bearer_to_token(store_token)})
    series_response = session.getMethod(v.FETCH_TV_SERIES) 

    if not series_response.ok:
        print(series_response.json())
        session.remove_parameter('Authorization')
        # To get new token
        response = session.login(my_id, my_password)  
        if response.ok:
            token = response.json()['token']
            session.update_parameter({'Authorization': add_bearer_to_token(token)})

            # Calling once more 
            series_response = session.getMethod(v.FETCH_TV_SERIES) 
            # Debug : Below 3 lines
        else:
            print("auth error occured!")
        print(response.json())

    # Getting the series details, e.g. no. of seasons, all episodes
    series_response_json = series_response.json()
    print_series_data(series_response_json) # Printing the name of the series and year
    print_extract_links(series_response_json, token) # NEED TO WORK ON THIS !!!!

if __name__ == '__main__':
    print('start')
    run()
