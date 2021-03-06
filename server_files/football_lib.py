class _football_API:
    # Initialize football API dictionaries
    def __init__(self):
        self.final_scores = dict()
        self.winning_scores = dict()
        self.losing_scores = dict()
        self.total_scores = dict()
        self.point_diffs = dict()
        self.teams = dict()
        self.dates = dict()

    # Load data into class dictionaries
    def load_data(self, filename):
        f = open(filename, "r")
        for line in f:
            # Grab date from each line
            line = line.rstrip()
            components = line.split(',')
            fid = int(components[0])
            final_score = components[1]
            winning_score = components[2]
            losing_score = components[3]
            total_score = components[4]
            point_diff = components[5]

            # Handle the Teams and Dates that are one string
            teams_and_date = components[6]
            components = teams_and_date.split(' ')
            team = ' '.join(components[:-3])
            date = ' '.join(components[-3:])

            # Add the data to the dictionaries
            self.final_scores[fid] = final_score
            self.winning_scores[fid] = winning_score
            self.losing_scores[fid] = losing_score
            self.total_scores[fid] = total_score
            self.point_diffs[fid] = point_diff
            self.teams[fid] = team
            self.dates[fid] = date

        f.close()
        
    # Pretty printing for an individual game
    def game_toDict(self, fid):
        fid = int(fid)
        try:
            gameDict = dict()
            gameDict['id'] = str(fid)
            gameDict['teams']  = self.teams[fid]
            gameDict['date']  = self.dates[fid]
            gameDict['finalScore'] = self.final_scores[fid]
            gameDict['winnerScore'] = self.winning_scores[fid]
            gameDict['loserScore'] = self.losing_scores[fid]
            gameDict['pointDiff'] = self.point_diffs[fid]
            gameDict['totalScore'] = self.total_scores[fid]

        except Exception as ex:
            gameDict = None
        
        return gameDict

    # Deletes a particular game from data set
    def delete_game(self, fid):
        self.final_scores.pop(fid)
        self.winning_scores.pop(fid)
        self.losing_scores.pop(fid)
        self.total_scores.pop(fid)
        self.point_diffs.pop(fid)
        self.teams.pop(fid)
        self.dates.pop(fid)

    # Returns the number of games in the data set
    def get_games(self):
        return len(self.final_scores)

    # Abbreviated set_game that changes the score of a game
    def change_score(self, fid, score):
        self.final_scores[fid] = score[0]
        self.winning_scores[fid] = score[1]
        self.losing_scores[fid] = score[2]
        self.total_scores[fid] = str(int(score[1]) + int(score[2]))
        self.point_diffs[fid] = str(int(score[1]) - int(score[2]))
    
    # Creates new game and appends to the dictionaries
    def set_game(self, fid, game):
        self.final_scores[fid] = game[0]
        self.winning_scores[fid] = game[1]
        self.losing_scores[fid] = game[2]
        self.total_scores[fid] = game[3]
        self.point_diffs[fid] = game[4]
        self.teams[fid] = game[5]
        self.dates[fid] = game[6]
