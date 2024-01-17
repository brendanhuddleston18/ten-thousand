import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        score = 0

        # Count occurrences of each number
        count_dict = {i: dice_roll.count(i) for i in range(1, 7)}

        # Check for a straight (1-6)
        if all(count == 1 for count in count_dict.values()):
            return 1500

        # Check for three pairs
        if len(count_dict) == 3 and all(count == 2 for count in count_dict.values()):
            return 1500

        # Check for two sets of three numbers
        if len(count_dict) == 2 and all(count == 3 for count in count_dict.values()):
            return 1500

        # Scoring for three or more of a kind
        for num, count in count_dict.items():
            if count >= 3:
                if num == 1:
                    score += 1000 + (count - 3) * 1000  # For ones
                else:
                    score += num * 100 + (count - 3) * (num * 100)  # For other numbers

        # Scoring for single ones and fives not part of a set
        if count_dict[1] < 3:
            score += count_dict[1] * 100
        if count_dict[5] < 3:
            score += count_dict[5] * 50

        return score

    @staticmethod
    def roll_dice(num_dice):
        # Ensure the input is between 1 and 6
        if not 1 <= num_dice <= 6:
            raise ValueError("Number of dice should be between 1 and 6")

        # Generate a tuple with random values between 1 and 6
        dice_roll = tuple(random.randint(1, 6) for _ in range(num_dice))
        return dice_roll