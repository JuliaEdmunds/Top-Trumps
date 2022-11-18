# Brief overview: class that contains all pokemon info

class Pokemon:
    def __init__(self, pokemon_id, name, stats):
        self.pokemon_id = pokemon_id
        self.name = name
        self.stats = stats

    def __str__(self):
        print_stats = ", ".join(f'{key}: {value}' for key, value in self.stats.items())
        return f"Name: {self.name}, id: {self.pokemon_id}, {print_stats}"
