
# Task 6

def at_the_movies(movie_choices):
    counts = {}
    for movie in movie_choices:
        counts[movie] = counts.get(movie, 0) + 1
    return counts

choices = ['Comedy', 'Action', 'Comedy', 'Drama', 'Action', 'Comedy']
print('Movie choice counts:', at_the_movies(choices))
