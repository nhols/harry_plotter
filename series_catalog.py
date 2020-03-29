import omdb_api
import pickle


# classics
simpsons_data = get_all_episodes({'i': 'tt0096697', 'apikey': API_KEY})
friends_data = get_all_episodes({'i': 'tt0108778', 'apikey': API_KEY})
smallville_data = get_all_episodes({'i': 'tt0279600', 'apikey': API_KEY})

# science and nature
frozen_planet_data = get_all_episodes({'i': 'tt2092588', 'apikey': API_KEY})
planet_earth_data = get_all_episodes({'i': 'tt0795176', 'apikey': API_KEY})
life_data = get_all_episodes({'i': 'tt1533395', 'apikey': API_KEY})
blue_planet_data = get_all_episodes({'i': 'tt0296310', 'apikey': API_KEY})
planet_earth_II_data = get_all_episodes({'i': 'tt5491994', 'apikey': API_KEY})
our_planet_data = get_all_episodes({'i': 'tt9253866', 'apikey': API_KEY})
cosmos_data = get_all_episodes({'i': 'tt0081846', 'apikey': API_KEY})

# comedy
the_office_us_data = get_all_episodes({'i': 'tt0386676', 'apikey': API_KEY})
the_office_uk_data = get_all_episodes({'i': 'tt0290978', 'apikey': API_KEY})
rick_and_morty_data = get_all_episodes({'i': 'tt2861424', 'apikey': API_KEY})

# drama
got_data = get_all_episodes({'i': 'tt0944947', 'apikey': API_KEY})
breaking_bad_data = get_all_episodes({'i': 'tt0903747', 'apikey': API_KEY})
mr_robot_data = get_all_episodes({'i': 'tt4158110', 'apikey': API_KEY})
walking_dead_data = get_all_episodes({'i': 'tt1520211', 'apikey': API_KEY})
westworld_data = get_all_episodes({'i': 'tt0475784', 'apikey': API_KEY})
black_mirror_data = get_all_episodes({'i': 'tt2085059', 'apikey': API_KEY})
chernobyl_data = get_all_episodes({'i': 'tt7366338', 'apikey': API_KEY})

# game shows
wwtbam_data = get_all_episodes({'i': 'tt0211178', 'apikey': API_KEY})
the_cube_data = get_all_episodes({'i': 'tt1555887', 'apikey': API_KEY})
takeshis_castel_data = get_all_episodes({'i': 'tt0375466', 'apikey': API_KEY})


data = [simpsons_data, friends_data, smallville_data,
        frozen_planet_data, planet_earth_data, life_data, blue_planet_data, planet_earth_II_data, our_planet_data, cosmos_data,
        the_office_us_data, the_office_uk_data, rick_and_morty_data,
        got_data, breaking_bad_data, mr_robot_data, walking_dead_data, westworld_data, black_mirror_data, chernobyl_data]

with open('series.data', 'wb') as filehandle:
    pickle.dump(data, filehandle)

with open('listfile.data', 'rb') as filehandle:
    data = pickle.load(filehandle)