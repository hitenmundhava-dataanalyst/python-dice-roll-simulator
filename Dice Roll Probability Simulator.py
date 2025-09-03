import random

# Dice class with OOP
class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
    
# Generator: simulate rolls and yield results
def dice_rolls(num_rolls, sides=6):
    dice = Dice(sides)
    for i in range(num_rolls):
        result = dice.roll()
        # Example: skip invalid attempts (say we don't allow rolling a 1)
        if result == 1:
            continue
        yield result

# Run the simulator
if __name__ == "__main__":
    rolls = list(dice_rolls(20))  # roll 20 times
    print("Roll results (skipping 1s):", rolls)

    # Probability simulation
    probability = {i: rolls.count(i) / len(rolls) for i in set(rolls)}
    print("Probabilities:", probability)