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
    session = Mysession() # Create a session

    session.update_parameter({'Authorization': add_bearer_to_token(token)})
    # series_response = session.getMethod(v.FETCH_TV_SERIES)
    print("Verifying token...")
    response = session.getMethod(v.HOME_API) # Check the status of cache_token

    if not response.ok:
        print(response.json())
        session.remove_parameter('Authorization')
        # To get new token
        print("Getting new token...")
        response = session.login(my_id, my_password)  
        if response.ok:
            token = response.json()['token']
            # Set the new token to env variables
            set_key(dotenv_file, "TOKEN", token)
            session.update_parameter({'Authorization': add_bearer_to_token(token)})
            
            # Debug : Below 3 lines
        else:
            print("auth error occured!")
            print(response.json())

    
    search_result_response = session.searchby_keyword(v.SEARCH_API, search_input())
    tv_id = print_search_results(search_result_response.json())

    series_response = session.getMethod(f'{v.FETCH_TV_SERIES}/{tv_id}')

    response_json_series = series_response.json() # Getting the series response in json format

    quality = confirm_quality(response_json_series)
    response_json_seasons = response_json_series["seasons"][quality]

    # Getting the series details, e.g. no. of seasons, all episodes
    print_series_data(series_json=response_json_series) # Printing the name of the series and year
    print_extract_links(response_json_seasons, token) # NEED TO WORK ON THIS !!!!

if __name__ == '__main__':
    run(token=cache_token)
    
