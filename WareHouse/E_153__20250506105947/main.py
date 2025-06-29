'''
Main entry point for the Spell Caster application.
'''
from spell import Spell
def main():
    '''
    Main function to execute the spell casting logic.
    '''
    # Read monster's health and number of spells
    H = int(input("Enter Monster's Health (H): "))
    N = int(input("Enter Number of Spells (N): "))
    spells = []
    # Read spell damage and cost pairs
    for i in range(N):
        damage, cost = map(int, input(f"Enter Spell {i + 1} Damage and Cost (space-separated): ").split())
        if damage <= 0 or cost <= 0:
            print("Error: Damage and Cost must be greater than zero. Please enter valid values.")
            return  # Exit the program or handle as needed
        spells.append(Spell(damage, cost))  # Use Spell class to create spell objects
    # Sort spells based on cost per damage ratio
    spells.sort(key=lambda spell: spell.cost / spell.damage)
    total_cost = 0
    # Calculate the minimum Magic Points consumed
    while H > 0:
        for spell in spells:
            # Calculate number of casts needed for the current spell
            casts = (H + spell.damage - 1) // spell.damage  # Calculate number of casts needed
            total_cost += casts * spell.cost  # Update total cost for the number of casts needed
            H -= casts * spell.damage  # Reduce health by the total damage dealt
            # Check if H is reduced to 0 or below after the cast
            if H <= 0:
                break  # Exit the loop if monster's health is 0 or below
    print(f"Minimum Magic Points Consumed: {total_cost}")
if __name__ == "__main__":
    main()