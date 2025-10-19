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
    """Finds the country of passed car name

    Args:
        matches - a list of x strings
    Returns:
        a list of the car's country(s)
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
        a list of car titles made after the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any cars made that year, only after)
    """

    rank = matches[0]
    result = []
    for car in cars_db:
        if get_country_rank(car) == rank:
            result.append(get_country(car))
    return result


def cars_by_population_rank(matches: List[str]) -> List[str]:
    """Finds director of car based on title

    Args:
        matches - a list of 1 string, just the title

    Returns:
        a list of 1 string, the director of the car
    """
    rank = matches[0]
    result = []
    for car in cars_db:
        if get_country_rank(car) == rank:
            for top in get_top_cars(car):
                result.append(top)
    return result


def top_car_by_population_rank(matches: List[str]) -> List[str]:
    """Finds cars directed by the passed in director

    Args:
        matches - a list of 1 string, just the director

    Returns:
        a list of cars titles directed by the passed in director
    """
    rank = matches[0]
    result = []
    for car in cars_db:
        if get_country_rank(car) == rank:
            result.append(get_top_cars(car)[0])
    return result

def population_rank_by_car(matches: List[str]) -> List[str]:
    """Finds the country of passed car name

    Args:
        matches - a list of 1 string
    Returns:
        a list of the car's country
    """
    example_car = matches[0]
    result = []
    for car in cars_db:
        for vehicle in get_top_cars(car):
            if vehicle == example_car:
                result.append(get_country_rank(car))
    return result

def cars_by_top_car(matches: List[str]) -> List[str]:
    """Finds second and third most sold cars for a given top car.
        Args:
            matches - a list of 1 string, just the car title

        Returns:
            a list of one item (an int), the year that the car was made
    """
    example_car = matches[0]
    result = []
    for car in cars_db:
        if example_car in get_top_cars(car):
            # Return the other cars from that same country
            result.extend(get_top_cars(car))
    return result

# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("What countries had _ as one of their most sold cars."), country_by_car),
    (str.split("What country is rank _ in population."), country_by_population_rank),
    (str.split("what were the top 3 most sold cars in the country with population rank _"), cars_by_population_rank),
    (str.split("What was the most sold car in the country with population rank _"), top_car_by_population_rank),
    (str.split("What population ranked nations had the _ as one of the most sold cars."), population_rank_by_car),
    (str.split("What were second and third most sold cars in the nation with the top car _"), cars_by_top_car),
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
    # Test 1: cars_by_country
    assert isinstance(cars_by_country(["India"]), list)
    assert "Maruti Suzuki Alto" in cars_by_country(["India"])

    # Test 2: top_car_by_country
    assert top_car_by_country(["Japan"]) == ["Toyota Corolla"]

    # Test 3: country_by_car
    assert country_by_car(["Toyota Corolla"]) == [
        "Pakistan", "Egypt", "Japan", "Bangladesh", "Poland", "Venezuela", "Uzbekistan"
    ]

    # Test 4: country_by_population_rank
    assert country_by_population_rank(["3"]) == ["United States"]

    # Test 5: cars_by_population_rank
    assert "Ford F-Series" in cars_by_population_rank(["3"])

    # Test 6: top_car_by_population_rank
    assert top_car_by_population_rank(["2"]) == ["Maruti Suzuki Alto"]

    # Test 7: population_rank_by_car
    assert population_rank_by_car(["Ford F-Series"]) == ["3"]

    # Test 8: cars_by_top_car
    assert sorted(cars_by_top_car(["Toyota Hilux"])) != [], "cars_by_top_car returned empty list"

    # Test 9: unmatched query
    assert search_pa_list(["nonsense", "query"]) == ["I don't understand"]

    # Test 10: bye keyword
    try:
        bye_action(["dummy"])
    except KeyboardInterrupt:
        pass
    else:
        raise AssertionError("bye_action did not raise KeyboardInterrupt")

    print("✅ All car database tests passed!")
