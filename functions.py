import variables as v
# For reference a standard link would look like:
# api_url/NAME/?id=_ID&token=TOKEN


# Prompt for confirmation on above series config
def prompt():
    print(f"""
    The tvSeriesid is: {v.TV_ID}
    """)

    user_input = input("Press enter to continue...")
    if user_input != "":
        raise SystemExit("Quitting")

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