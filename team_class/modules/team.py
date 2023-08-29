class Team:
    def __init__(self, name_of_team, list_of_players, name_of_coach):

        self.name = name_of_team
        self.players = list_of_players
        self.coach = name_of_coach
        self.points = 0
    
    

    def add_player(self, new_player):

        self.players.append(new_player)


    def has_player(self, input_player):

        return input_player in self.players
    

    def play_game(self, result):

        if result == True:
            self.points += 3
            

    

