import random

class Films:
    def __init__(self, title, publication_date, species, number_of_plays):
        self.title = title
        self.publication_date = publication_date
        self.species = species
        self.number_of_plays = number_of_plays

        self.current_plays = 0

    def __str__(self):
        return f'{self.title}'
    
    def message(self):
        return f'{self.title} {self.publication_date}'

    def play(self):
        self.current_plays += 1

class Series(Films):
    def __init__(self, episode_nr, season_nr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_nr = episode_nr
        self.season_nr = season_nr

    def __str__(self):
        return f'{super().__str__()} {self.season_nr}{self.episode_nr}'
    
films_series_list = [Films('Incepcja', 2010, 'Thriller', 150000), Films('Zielona Mila', 1999, 'Dramat', 180000),
                      Series('05', '01', 'Breaking Bad', 2008, 'Dramat', 300000), Series('06', '10', 'Friends', 1994, 'Sitcom', 600000)]


def get_movies():
    films_only = []
    for i in films_series_list:
        if isinstance(i, Films) and not isinstance(i, Series):
            films_only.append(i)
    sorted_films = sorted(films_only, key=lambda x: x.title)
    return sorted_films
    
def get_series():
    series_only = []
    for i in films_series_list:
        if isinstance(i, Series):
            series_only.append(i)
    sorted_series = sorted(series_only, key=lambda x: x.title)
    return sorted_series

def search(name):
    for movie in films_series_list:
        if movie.title == name:
            return movie
        
def generate_views():
    choice = random.choice(films_series_list)
    choice.current_plays = random.randint(0, 101)
    return choice

def run():
    for i in range(10):
        generate_views()

def top_title():
    max_plays = max(films_series_list, key = lambda x: x.number_of_plays)
    for movie in films_series_list:
        if movie == max_plays:
            return movie


if __name__ == '__main__':
    print(len(films_series_list))
    print(get_movies()[0].title)
    print(get_series()[0].title)
    print(search('Breaking Bad'))
    print(generate_views().current_plays)
    run()
    print(top_title())