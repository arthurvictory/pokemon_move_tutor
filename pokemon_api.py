import requests
from random import randint

class Pokemon:
    def __init__(self, name):
        self.name = name.lower()
        self.poke_api_call(name)

    def poke_api_call(self, name):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        if r.status_code == 200:
            pokemon = r.json()
        else:
            print(f"Please check the spelling of your pokemon's name and try again!: {r.status_code}")
            return
        self.name = pokemon['name']
        self.move_list = [move['move']['name'] for move in pokemon['moves']]
        print(f"{self.name}'s info has been updated")
        print(self.move_list)

class Move_Tutor(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.taught_moves = []

    def teach_move(self):
        moves = len(self.move_list) + len(self.taught_moves)
        random = randint(1, 900)
        if moves > 4:
            return print(f"You know too many moves!")
        else:
            url = f"https://pokeapi.co/api/v2/move/{random}"
            r = requests.get(url)
            if r.ok:
                data = r.json()
                move_to_teach = data['name']
                if move_to_teach in self.move_list:
                    return print(f"You already know that {move_to_teach}!")
                else:
                    self.taught_moves.append(move_to_teach)
                  
            else:
                return print("Bad request!")
        print(f"Here are all the moves you've been taught: {self.taught_moves}")

teaching = Move_Tutor('onix')
teaching.teach_move()