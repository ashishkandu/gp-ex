import variables as v
# For reference a standard link would look like:
# api_url/NAME/?id=_ID&token=TOKEN
# https://apis.googolplex.live/api/drive/download/Friends.S01E01.The.One.where.Monica.Gets.a.New.Roomate.720p.BluRay.2CH.x265.HEVC-PSA.mkv?id=5f38c11c42e04400042e641c&token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiTWFkYXJjaG9kLCB0b2tlbiBreXUgZGVjb2RlIGtpeWEgYmU_IiwiaWF0IjoxNjY3NzIyMzE4LCJleHAiOjE2Njc3MjU5MTh9.E2o3oJmSe4RU2vuoZRlmmwgbgEi8UdRHaYGsDvG16t0s6RfYfN6BH0orgBNz8EnFubFL7XnbmYVw-5Nx6JLQHcXGgcHoFGbDc8f2i5f5WCS7MOoDCFY05EYNIVIJOM_xWHhGaJrbWEdc1pgPsBoF4Yt_uaukiFCz6KV5kHbmQADDV6kgIH9AZW4WrvG8SFcvX5B7HxfdHVAu61aMOIBbD6oufzozLYHPm9l8fHbHN0AG2wRIwTwLS6nleS8ht2DkCEg-u_9b-RZz1BAjFBnLPBX65BdmYMj4_ttLRUcuz_HP4BnAhlXoWQ9J20lP8BJTrItdbUBtbO0NJ0a4lZ6DI4MEkYFR7448RDUsBxDZI1JrXNFzTDk0YDcaB6uiNMaFwPJci7Uj_e8Ukfwg8BZPIiJm8XAlR1gwhRJscD_3J29iDKFBtkj0mkdfsJgVu71Gn8A1dK8BattrLPdI-bl7tHH0s6pVU1H7zggvJ6IJaAdLTzZCaaSzObON8NcxGwVuD7Sk8wD1bHZhy_irkd3MdFtY9i_x6oUWjMMO9nKtXJWsldUsrUcTmIcNTPFqVFmOrHhFS-ZARbb8XE_n29uwxmDVePhRHyTfjGqGnVu5q2M2T0idFDyQqGjoZE2RpZYtUtHKrpPEa77C4OOkAC75p2dJ8gJaGVPOV-v8p3Ij5rs


# Prompt for confirmation on above series config
def prompt():
    print(f"""
    The quality is set to: {v.QUALITY}p
    It Contains: {v.TOTAL_SEASONS} Seasons
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


def get_season_count(series_json_data):
    return len(series_json_data["seasons"][v.QUALITY])


def print_extract_links(series_json: dict, token):
    # Looping for total_seasons and generating downloadable links with token attached
    seasons = get_season_count(series_json)
    for season_no in range(1, seasons + 1):
        season = series_json["seasons"][v.QUALITY][str(season_no)]["episodes"]

        links = list()

        for episode in season:
            formatted_link = f'{v.DOWNLOAD_API}/{episode["name"]}?id={episode["_id"]}&token={token}'
            links.append(formatted_link)
        print(f"Season {season_no}:\n")
        print(links)
        print("\n\n")