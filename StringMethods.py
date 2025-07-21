SHOWS = [
   " Married at first sight",
   " temptation Island",
         "Love is blind",
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip(). title())

        print(', '.join(cleaned_shows))
    
main()