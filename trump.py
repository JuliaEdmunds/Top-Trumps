# Brief overview: class that contains all card info

class Card:
    def __init__(self, card_id, name, stats):
        self.card_id = card_id
        self.name = name
        self.stats = stats

    def __str__(self):
        print_stats = ", ".join(f'{key}: {value}' for key, value in self.stats.items())
        return f"Name: {self.name} (id: {self.card_id}), available stats to choose from: {print_stats}"
