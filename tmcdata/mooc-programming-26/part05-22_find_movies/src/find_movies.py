# Write your solution here
def find_movies(database: list, search_term: str):
    results = []

    for movie in database:
        if search_term.lower() in movie["name"].lower():
            results.append(movie)

    return results