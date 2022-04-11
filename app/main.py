import os
from pathlib import Path
from collections import defaultdict
from pprint import pprint


class Ranking:
    """calculates the ranking table for a league"""
    def __init__(self, **data):
        self.__dict__.update(data)

    def rank(self):
        """Create a ranking list"""
        scores = self.__dict__['league'] # explicit parsing, single input argument
        teams = defaultdict(list)

        for _match in scores:
            _teams = _match.split(',')

            tmp = {}
            for team in _teams:
                team = team.strip().split(" ")
                name = " ".join(team[:-1])
                score = int(team[-1])
                tmp[name] = score

            scores = list(tmp.values())
            names = list(tmp.keys())

            # rules
            for i in range(len(scores) - 1):
                if scores[i] == scores[i+1]:
                    teams[names[i]].append(1)
                    teams[names[i+1]].append(1)
                elif scores[i] > scores[i+1]:
                    teams[names[i]].append(3)
                    teams[names[i+1]].append(0)

        count_scores = {}
        for team, score in teams.items():
            count_scores[team] = sum(score)
        # sort dictionary by scores
        count_scores = sorted(count_scores.items(), key=lambda item: item[1], reverse=True)

        # sort alphabetically
        for i in range(len(count_scores)):
            try:
                if count_scores[i][-1] == count_scores[i+1][-1]:
                    # check alphabetical order
                    tmp = sorted([count_scores[i], count_scores[i+1]], key=lambda item: item[0])
                    count_scores[i], count_scores[i+1] = tmp[0], tmp[1]
            except IndexError as e:
                _ = e # log error

        self.__dict__.update({'ranked': count_scores})


    def display_table(self):
        """Format output"""
        table = self.__dict__['ranked']
        count = 1

        for team in table:
            if team[1] == 1:
                _pt = "pt"
            else:
                _pt = "pts"

            print("{count}. {name}, {score} {plc}".format(count=count, name=team[0], score=team[1], plc=_pt))
            count += 1

    def __repr__(self):
        inputs = []

        for k, v in self.__dict__.items():
            inputs.append("{}={}".format(k, v))

        return "{}({})".format(type(self).__name__, ", ".join(inputs))


def get_data():
    """Get input data stdio or file"""

    while(True):
        try:
            prompt = eval(input("Input data, if stdio [1] else if filename [2]: "))
        except NameError as e:
            print("Wrong input inserted")

        try:
            assert type(prompt) == type(1)
            input_data = []
            if prompt == 1:
                # stdio data
                Flag = True
                print("Terminal inputs")

                while(Flag):
                    get_input = input("Enter match scores (e.g Lions 3, Snakes 3), q to quit: ")
                    if get_input == 'q':
                        Flag = False
                    else:
                        input_data.append(get_input)
                        print(input_data)
            elif prompt == 2:
                # file data input
                print("Input data from file")
                filename = input("Enter filename: ") # no need to add special handling here
                relative_path = Path(os.path.dirname(__file__))
                filename = os.path.join(relative_path, filename)

                with open(filename, 'r') as data:
                    input_data = [l.strip() for l in data.readlines() if ',' in l]

            return input_data
        except NameError as e:
            print(e)


if __name__ ==  "__main__":
    print("League Table Ranking")
    input_data = get_data()
    ranking = Ranking(league=input_data)
    print(repr(ranking))
    ranking.rank()
    ranking.display_table()

