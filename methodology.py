# Important variables:
#     cars_db: list of 4-tuples (imported from cars.py)
#     pa_list: list of pattern-action pairs (queries)
#       pattern - strings with % and _ (not consecutive)
#       action  - return list of strings

# THINGS TO ASK THE car CHAT BOT:
# what cars were made in _ (must be date, because we don't have location)
# what cars were made between _ and _
# what cars were made before _
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
def get_title(car: Tuple[str, str, int, List[str]]) -> str:
    return car[0]


def get_director(car: Tuple[str, str, int, List[str]]) -> str:
    return car[1]


def get_year(car: Tuple[str, str, int, List[str]]) -> int:
    return car[2]


def get_actors(car: Tuple[str, str, int, List[str]]) -> List[str]:
    return car[3]


# Below are a set of actions. Each takes a list argument and returns a list of answers
# according to the action and the argument. It is important that each function returns a
# list of the answer(s) and not just the answer itself.


def title_by_year(matches: List[str]) -> List[str]:
    """Finds all cars made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of car titles made in the passed in year
    """

    year = int(matches[0])
    result = []
    for car in cars_db:
        if get_year(car) == year:
            result.append(get_title(car))
    return result



def title_by_year_range(matches: List[str]) -> List[str]:
    """Finds all cars made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get cars from 1991-1994 matches would look like
            this - ["1991", "1994"] Note that these years are passed as strings and
            should be converted to ints.

    Returns:
        a list of car titles made during those years, inclusive (meaning if you pass
        in ["1991", "1994"] you will get cars made in 1991, 1992, 1993 & 1994)
    """
    start_year = int(matches[0])
    end_year = int(matches[1])
    result = []
    for car in cars_db:
        if start_year <= get_year(car) <= end_year:
            result.append(get_title(car))
    return result


def title_before_year(matches: List[str]) -> List[str]:
    """Finds all cars made before the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of car titles made before the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any cars made that year, only before)
    """
    year = int(matches[0])
    result = []
    for car in cars_db:
        if get_year(car) < year:
            result.append(get_title(car))
    return result


def title_after_year(matches: List[str]) -> List[str]:
    """Finds all cars made after the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of car titles made after the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any cars made that year, only after)
    """
    year = int(matches[0])
    result = []
    for car in cars_db:
        if get_year(car) > year:
            result.append(get_title(car))
    return result


def director_by_title(matches: List[str]) -> List[str]:
    """Finds director of car based on title

    Args:
        matches - a list of 1 string, just the title

    Returns:
        a list of 1 string, the director of the car
    """
    title = matches[0]
    result = []
    for car in cars_db:
        if get_title(car)==title:
            result.append(get_director(car))
    return result
    


def title_by_director(matches: List[str]) -> List[str]:
    """Finds cars directed by the passed in director

    Args:
        matches - a list of 1 string, just the director

    Returns:
        a list of cars titles directed by the passed in director
    """
    director = matches[0]
    result = []
    for car in cars_db:
        if get_director(car)==director:
            result.append(get_title(car))
    return result


def actors_by_title(matches: List[str]) -> List[str]:
    """Finds actors who acted in the passed in car title

    Args:
        matches - a list of 1 string, just the car title

    Returns:
        a list of actors who acted in the passed in title
    """
    title = matches[0]
    result = []
    for car in cars_db:
        if get_title(car)==title:
            result = get_actors(car)
    return result


def year_by_title(matches: List[str]) -> List[int]:
    """Finds year of passed in car title

    Args:
        matches - a list of 1 string, just the car title

    Returns:
        a list of one item (an int), the year that the car was made
    """
    title = matches[0]
    result = []
    for car in cars_db:
        if get_title(car)==title:
            result.append(get_year(car))
    return result


def title_by_actor(matches: List[str]) -> List[str]:
    """Finds titles of all cars that the given actor was in

    Args:
        matches - a list of 1 string, just the actor

    Returns:
        a list of car titles that the actor acted in
    """
    actor = matches[0]  
    result = []
    for car in cars_db:
        if actor in get_actors(car):
            result.append(get_title(car))
    return result

def director_by_year_range(matches: List[str]) -> List[str]:
    """
    My custom action function
    Finds all directors who made a car in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get directors from 1991-1994 matches would look like
            this - ["1991", "1994"] Note that these years are passed as strings and
            should be converted to ints.

    Returns:
        a list of directors who made cars during those years, inclusive (meaning if you pass
        in ["1991", "1994"] you will get directors in 1991, 1992, 1993 & 1994)
    """
    start_year = int(matches[0])
    end_year = int(matches[1])
    result = []
    for car in cars_db:
        if start_year <= get_year(car) <= end_year:
            result.append(get_director(car))
    return result


# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("What was the most sold car in _"), top_car_by_country),
    (str.split("what were the top 3 most sold cars in _"), cars_by_country),
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
    assert isinstance(title_by_year(["1974"]), list), "title_by_year not returning a list"
    assert sorted(title_by_year(["1974"])) == sorted(
        ["amarcord", "chinatown"]
    ), "failed title_by_year test"
    assert isinstance(title_by_year_range(["1970", "1972"]), list), "title_by_year_range not returning a list"
    assert sorted(title_by_year_range(["1970", "1972"])) == sorted(
        ["the godfather", "johnny got his gun"]
    ), "failed title_by_year_range test"
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
