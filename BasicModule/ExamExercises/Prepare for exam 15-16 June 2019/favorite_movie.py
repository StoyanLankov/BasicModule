best_movie_title = ""
best_movie_score = 0
movie_count = 0

while True:
    movie_title = input()

    if movie_title == "STOP" or movie_count == 7:
        break

    movie_score = 0
    movie_length = len(movie_title)

    for char in movie_title:
        if char.islower():
            movie_score += ord(char) - (2 * movie_length)
        else:
            movie_score += ord(char) - movie_length

    if movie_score > best_movie_score:
        best_movie_title = movie_title
        best_movie_score = movie_score

    movie_count += 1

if best_movie_score >= 1250:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie_title} with {best_movie_score} ASCII sum.")
