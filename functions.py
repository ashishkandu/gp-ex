import variables as v
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
    print(f"{series_json['name']} ({series_json['imdbData']['Year']})")
    print("\n")


def confirm_quality(series_json):
    for index, q in enumerate(series_json["quality"], start=1): print(f'{index}. {q}')
    while True:
        try:
            choice = int(input('\nPlease choose the quality: '))
            if choice > len(series_json["quality"]): 
                print("Please choose from above option!")
                continue
        except ValueError:
            print("Please enter numbers only...")
        except KeyboardInterrupt:
            raise SystemExit("Quit!")
        else:
            return series_json["quality"][choice - 1]

def print_extract_links(json_seasons: dict, token):
    # Looping for total_seasons and generating downloadable links with token attached
    for season_no in range(1, len(json_seasons) + 1):
        season = json_seasons[str(season_no)]["episodes"]

        links = list()

        for episode in season:
            formatted_link = f'{v.DOWNLOAD_API}/{episode["name"]}?id={episode["_id"]}&token={token}'
            links.append(formatted_link)
        print(f"Season {season_no}:\n")
        print(links)
        print("\n\n")