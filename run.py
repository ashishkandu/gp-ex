from functions import *
from mysession import Mysession
from dotenv import load_dotenv, set_key, find_dotenv
import variables as v
import os

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)
my_id = os.getenv('USER_NAME')
my_password = os.getenv('PASSWORD')
cache_token = os.getenv('TOKEN')

def run(token):
    prompt() # A prompt for confirmation of variables set
    session = Mysession() # Create a session

    session.update_parameter({'Authorization': add_bearer_to_token(token)})
    series_response = session.getMethod(v.FETCH_TV_SERIES) 

    if not series_response.ok:
        print(series_response.json())
        session.remove_parameter('Authorization')
        # To get new token
        response = session.login(my_id, my_password)  
        if response.ok:
            token = response.json()['token']
            # Set the new token to env variables
            set_key(dotenv_file, "TOKEN", token)

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
    run(token=cache_token)
    
