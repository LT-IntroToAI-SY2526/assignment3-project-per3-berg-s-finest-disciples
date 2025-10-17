# Important variables:
#     cars_db: list of 4-tuples (imported from cars.py)
#     pa_list: list of pattern-action pairs (queries)
#       pattern - strings with % and _ (not consecutive)
#       action  - return list of strings

# THINGS TO ASK THE car CHAT BOT:
# what cars were made in _ (country)
# what best car was made in _ (country)
# what country was _ made in? (car)
# what cars were made after _
# who directed %
# who was the director of %
# what cars were directed by %
# who acted in %
# when was % made
# in what cars did % appear
# bye

#  Include the car database, named cars_db
from cars import cars_db
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "car" (a tuple)
def get_country(car: Tuple[str, str, int, List[str]]) -> str:
    return car[0]


def get_country_rank(car: Tuple[str, str, int, List[str]]) -> str:
    return car[1]


def get_year(car: Tuple[str, str, int, List[str]]) -> int:
    return car[2]


def get_top_cars(car: Tuple[str, str, int, List[str]]) -> List[str]:
    return car[3]


# Below are a set of actions. Each takes a list argument and returns a list of answers
# according to the action and the argument. It is important that each function returns a
# list of the answer(s) and not just the answer itself.


def top_car_by_country(matches: List[str]) -> List[str]:
    """Finds the top car made in the country in 2023.

    Args:
        matches - a list of 1 string, just the country

    Returns:
        a list of the top car made in the passed country
    """

    country = matches[0]
    result = []
    for car in cars_db:
        if get_country(car) == country:
            result.append((get_top_cars(car))[0])
    return result



def cars_by_country(matches: List[str]) -> List[str]:
    """Finds the top cars made in the country in 2023.

    Args:
        matches - a list of 1 string, just the country

    Returns:
        a list of cars made in the passed country
    """
    
    country = matches[0]
    result = []
    for car in cars_db:
        if get_country(car) == country:
            for top in get_top_cars(car):
                result.append(top)
    return result


def country_by_car(matches: List[str]) -> List[str]:
    """Finds the countries of passed car name

    Args:
        matches - a list of 1 string
    Returns:
        a list of the car's countries
    """
    example_car = matches[0]
    result = []
    for car in cars_db:
        for vehicle in get_top_cars(car):
            if vehicle == example_car:
                result.append(get_country(car))
    return result


def country_by_population_rank(matches: List[str]) -> List[str]:
    """Finds country based on population rank

    Args:
        matches - a list of 1 string, just the rank

    Returns:
        a list of car titles made in the country of the passed in rank
    """

    rank = matches[0]
    result = []
    for car in cars_db:
        if get_country_rank(car) == rank:
            for country in get_country(car):
                result.append(country)
    return result


def cars_by_population_rank(matches: List[str]) -> List[str]:
    """Finds top cars based on rank

    Args:
        matches - a list of 1 string, just the rank

    Returns:
        a list of top cars
    """
    rank = matches[0]
    result = []
    for car in cars_db:
        if get_country_rank(car) == rank:
            for top in get_top_cars(car):
                result.append(top)
    return result


def top_car_by_population_rank(matches: List[str]) -> List[str]:
    """Finds number 1 car from country by passed rank

    Args:
        matches - a list of 1 string, rank

    Returns:
        a list with the top car
    """
    rank = matches[0]
    result = []
    for car in cars_db:
        if get_country_rank(car) == rank:
            result.append(get_top_cars(car)[0])
    return result

def population_rank_by_car(matches: List[str]) -> List[str]:
    """Finds the country ranks of passed car name

    Args:
        matches - a list of 1 string
    Returns:
        a list of the car's country ranks
    """
    example_car = matches[0]
    result = []
    for car in cars_db:
        for vehicle in get_top_cars(car):
            if vehicle == example_car:
                result.append(get_country_rank(car))
    return result

def top_cars_by_one_car(matches: List[str]) -> List[int]:
    """Finds the cars based off of passed top car

    Args:
        matches - a list of 1 string, just the car 

    Returns:
        a list of cars
    """
    example_car = matches[0]
    result = []
    for car in cars_db:
        for vehicle in get_top_cars(car):
            if vehicle == example_car:
                for top in get_top_cars(car):
                    result.append(top)
    return result
    

# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
<<<<<<< HEAD
    (str.split("what cars were made in _"), car_by_country),
    (str.split("what cars were made between _ and _"), car_by_country_range),
=======
    (str.split("What was the most sold car in _"), top_car_by_country),
    (str.split("what were the top 3 most sold cars in _"), cars_by_country),
>>>>>>> 87e937151287bb2c2a3f21dec4ea540747c0613d
    (str.split("what directors were made between _ and _"), director_by_year_range),
    (str.split("what cars were made before _"), title_before_year),
    (str.split("what cars were made after _"), title_after_year),
    # note there are two valid patterns here two different ways to ask for the director
    # of a car
    (str.split("who directed %"), director_by_title),
    (str.split("who was the director of %"), director_by_title),
    (str.split("what cars were directed by %"), title_by_director),
    (str.split("who acted in %"), actors_by_title),
    (str.split("when was % made"), year_by_title),
    (str.split("in what cars did % appear"), title_by_actor),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pattern, act in pa_list:
        matching = match(pattern,src)

        if matching is not None:
            answer = act(matching)
            return answer if answer else ['No answers']
        
    return ["I don't understand"]


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the car database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


# uncomment the following line once you've written all of your code and are ready to try
# it out. Before running the following line, you should make sure that your code passes
# the existing asserts.
# query_loop()

if __name__ == "__main__":
    assert isinstance(car_by_country(["1974"]), list), "car_by_country not returning a list"
    assert sorted(car_by_country(["1974"])) == sorted(
        ["amarcord", "chinatown"]
    ), "failed car_by_country test"
    assert isinstance(car_by_country_range(["1970", "1972"]), list), "car_by_country_range not returning a list"
    assert sorted(car_by_country_range(["1970", "1972"])) == sorted(
        ["the godfather", "johnny got his gun"]
    ), "failed car_by_country_range test"
    assert isinstance(title_before_year(["1950"]), list), "title_before_year not returning a list"
    assert sorted(title_before_year(["1950"])) == sorted(
        ["casablanca", "citizen kane", "gone with the wind", "metropolis"]
    ), "failed title_before_year test"
    assert isinstance(title_after_year(["1990"]), list), "title_after_year not returning a list"
    assert sorted(title_after_year(["1990"])) == sorted(
        ["boyz n the hood", "dead again", "the crying game", "flirting", "malcolm x"]
    ), "failed title_after_year test"
    assert isinstance(director_by_title(["jaws"]), list), "director_by_title not returning a list"
    assert sorted(director_by_title(["jaws"])) == sorted(
        ["steven spielberg"]
    ), "failed director_by_title test"
    assert isinstance(title_by_director(["steven spielberg"]), list), "title_by_director not returning a list"
    assert sorted(title_by_director(["steven spielberg"])) == sorted(
        ["jaws"]
    ), "failed title_by_director test"
    assert isinstance(actors_by_title(["jaws"]), list), "actors_by_title not returning a list"
    assert sorted(actors_by_title(["jaws"])) == sorted(
        [
            "roy scheider",
            "robert shaw",
            "richard dreyfuss",
            "lorraine gary",
            "murray hamilton",
        ]
    ), "failed actors_by_title test"
    assert sorted(actors_by_title(["car not in database"])) == [], "failed actors_by_title not in database test"
    assert isinstance(year_by_title(["jaws"]), list), "year_by_title not returning a list"
    assert sorted(year_by_title(["jaws"])) == sorted(
        [1975]
    ), "failed year_by_title test"
    assert isinstance(title_by_actor(["orson welles"]), list), "title_by_actor not returning a list"
    assert sorted(title_by_actor(["orson welles"])) == sorted(
        ["citizen kane", "othello"]
    ), "failed title_by_actor test"
    
    
    assert sorted(search_pa_list(["hi", "there"])) == sorted(
        ["I don't understand"]
    ), "failed search_pa_list test 1"
    assert sorted(search_pa_list(["who", "directed", "jaws"])) == sorted(
        ["steven spielberg"]
    ), "failed search_pa_list test 2"
    assert sorted(
        search_pa_list(["what", "cars", "were", "made", "in", "2020"])
    ) == sorted(["No answers"]), "failed search_pa_list test 3"

    print("All tests passed!")
