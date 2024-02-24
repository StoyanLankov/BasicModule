num_movies = int(input())

max_rating = 0
max_movie = ""
min_rating = 10
min_movie = ""
total_rating = 0

for _ in range(num_movies):
    movie_name = input()
    movie_rating = float(input())

    if movie_rating > max_rating:
        max_rating = movie_rating
        max_movie = movie_name

    if movie_rating < min_rating:
        min_rating = movie_rating
        min_movie = movie_name

    total_rating += movie_rating

average_rating = total_rating / num_movies

print(f"{max_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
