import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate score determines the score of the user's dice roll 

        Parameters:
        - 6x Dice rolls determined by dice roll function

        Returns:
        - Score based dice roll
        """
        score = 0
        counts = {x: dice_roll.count(x) for x in set(dice_roll)}

        # Check for straight
        if len(counts) == 6:
            return 1500

        # Check for three pairs
        if len(counts) == 3 and all(count == 2 for count in counts.values()):
            return 1500

        # Check for two trios
        if len(counts) == 2 and all(count == 3 for count in counts.values()):
            return sum(100 * num if num != 1 else 1000 for num in counts)

        for num, count in counts.items():
            # Check for three or more of a kind
            if count >= 3:
                score += (num * 100) if num != 1 else 1000
                for _ in range(4, count + 1):
                    score += (num * 100) if num != 1 else 1000

            # Check for leftover ones and fives
            if num == 1 and count < 3:
                score += count * 100
            elif num == 5 and count < 3:
                score += count * 50

        return score


    @staticmethod
    def roll_dice(num_dice):
        """
        Dice Roll creates 6 random numbers to be used in the calculate score function

        Parameters:
        - Takes in the number of dice to be rolled

        Returns:
        - 6 integers that act as rolled dice
        """
        if 1 <= num_dice <= 6:
            return tuple(random.randint(1, 6) for _ in range(num_dice))
        else:
            raise ValueError("Number of dice must be between 1 and 6")
