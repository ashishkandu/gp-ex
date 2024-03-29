import json

# For reference a standard link would look like:
# api_url/NAME/?id=_ID&token=TOKEN

def search_input():
    while True:
        user_input = input("\nSearch for... ")
        if user_input == "":
            print("Cannot be empty!")
            continue
        return user_input


def print_search_results(search_results_json):
    results_len = len(search_results_json)
    if results_len == 0:
        raise SystemExit("Nothing found!")
    if results_len == 1:
        return search_results_json[0]["id"]
    print("\n")
    for index, items in enumerate(search_results_json, start=1):
        print(f'{index}. {items["title"]} - {items["id"]}')
        print()
        print(items["overview"])
        print(f'To check the poster -> {items["poster_path"]}')
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    while True:
        try:
            choice = int(input('\nPlease choose the result: '))
            if choice > results_len:
                print("Please choose from above option!")
                continue
        except ValueError:
            print("Please enter numbers only...")
        except KeyboardInterrupt:
            raise SystemExit("Quit!")
        else:
            return search_results_json[choice - 1]["id"]


def add_bearer_to_token(token):
    return "Bearer " + token


def print_series_data(series_json: dict):
    print("\n")
    year_start = series_json['imdbData']['Year'][:4]
    print(f"{series_json['name']} ({year_start})\n")


def confirm_quality(series_json):
    print_series_data(series_json=series_json)
    print("Available quality: ")
    for index, q in enumerate(series_json["quality"], start=1): print(f'{index}. {q}')
    while True:
        try:
            choice = int(input('\nPlease choose the quality: '))
            if choice > len(series_json["quality"]): 
                print("No choices with this number.")
                continue
        except ValueError:
            print("This value must match an existing value.")
        except KeyboardInterrupt:
            raise SystemExit("Quit!")
        else:
            return series_json["quality"][choice - 1]

def print_extract_links(json_seasons: dict, token, download_url):
    # Looping for total_seasons and generating downloadable links with token attached
    seasons = dict()
    for season in json_seasons:
        episodes = json_seasons[season]["episodes"] #json_seasons= response["seasons"][quality]

        season_episode_links = list()

        for episode in episodes:
            formatted_link = f'{download_url}/{episode["name"]}?id={episode["_id"]}&token={token}'
            season_episode_links.append(formatted_link)
        # print(f"Season {season}:\n")
        # print(season_episode_links)
        # print("\n\n")
        seasons[season] = season_episode_links
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(seasons, f, indent=4)
    # Temp work for pointing to the written file
    for key, values in seasons.items():
        print(f'Season {key}: {len(values)} episodes')
    print("Open -> /home/ashish/Contents/PythonScripts/playground/scrap_googolplex/output.json")