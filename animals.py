# Step 1: Create an Animal base class
# the class should support "name" and "year_discovered" properties


# Step 2: Create a Mamal class that inherits from your Animal base class
# be sure to create the class variables move, breathe and reproduce and assign
# the values descirbed in the README for this animal type.


# Step 3: Create a Bird class and that inherits from your Animal base class
# be sure to create the class variables move, breathe and reproduce and assign
# the values descirbed in the README for this animal type.


# Step 4: Create a Fish class that inherits from your Animal base class
# be sure to create the class variables move, breathe and reproduce and assign
# the values descirbed in the README for this animal type.

# ======================================================
# DECALRE ALL CLASSES OUTSIDE OF THE MAIN FUNCTION!
# ======================================================
def main():
    mamals_list = [
        {"name": "Panda", "year": 1869},
        {"name": "Zebra", "year": 1778},
        {"name": "Koala", "year": 1816},
        {"name": "Sloth", "year": 1804},
        {"name": "Armadillo", "year": 1758},
        {"name": "Raccoon", "year": 1758},
        {"name": "BigFoot", "year": 2021},
    ]

    birds_list = [
        {"name": "Pigeon", "year": 1837},
        {"name": "Peacock", "year": 1821},
        {"name": "Toucan", "year": 1758},
        {"name": "Parrot", "year": 1824},
        {"name": "Swan", "year": 1758},
    ]

    fishes_list = [
        {"name": "Salmon", "year": 1758},
        {"name": "Catfish", "year": 1817},
        {"name": "Perch", "year": 1758},
    ]

    # Step 5: loop through the list's above, and add each object created to the **animalsList** list
    animalsList = []

    # =============================================================================================================================
    # READ FIRST!!!!
    #
    # Below are a series of functions that need to be implemeneted.
    # Be sure you are NOT altering a list in place rather creating a new one
    # and assigning your result to the **sorted_animals** list
    # when solving each problem
    #
    # HINT: https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
    # =============================================================================================================================

    # =============================================================================================
    # Step 7: Goto the function orderByYearNamedDesc and follow the instructions
    # =============================================================================================
    # DO NOT CHNAGE
    print("=== List all the animals in descending order by year named ===")
    animals = orderByYearNamedDesc(animalsList)
    # =============================================================================================
    # on the line below, loop through the *animals* list and print each animal

    # =============================================================================================
    # Step 8: Goto the function sortAnimalsByName and follow the instructions
    # =============================================================================================
    # DO NOT CHNAGE
    print("\n\n=== List all the animals alphabetically ===")
    animals = sortAnimalsByName(animalsList)
    # =============================================================================================
    # on the line below, loop through the *animals* list and print each animal

    # =============================================================================================
    # Step 9: Goto the function sortAnimalsByMovement and follow the instructions
    # =============================================================================================
    # DO NOT CHNAGE
    print("\n\n=== List all the animals order by how they move ===")
    animals = sortAnimalsByMovement(animalsList)
    # =============================================================================================
    # on the line below, loop through the *animals* list and print each animal

    # =============================================================================================
    # Step 10: Goto the function findAnimalsWithLungs and follow the instructions
    # =============================================================================================
    # DO NOT CHNAGE
    print("\n\n=== List only those animals that breath with lungs ===")
    animals = findAnimalsWithLungs(animalsList)
    # =============================================================================================
    # on the line below, loop through the *animals* list and print each animal

    # =============================================================================================
    # Step 11: Goto the function findByLungsAndYear and follow the instructions
    # =============================================================================================
    # DO NOT CHNAGE
    print(
        "\n\n=== List only those animals that breath with lungs and were named in 1758 ==="
    )
    animals = findByLungsAndYear(animalsList)
    # =============================================================================================
    # on the line below, loop through the *animals* list and print each animal

    # =============================================================================================
    # Step 12: Goto the function findByEggsAndLungs and follow the instructions
    # =============================================================================================
    # DO NOT CHNAGE
    print("\n\n=== List only those animals that lay eggs and breath with lungs ===")
    animals = findByEggsAndLungs(animalsList)
    # =============================================================================================
    # on the line below, loop through the *animals* list and print each animal

    # =============================================================================================
    # Step 13: Goto the function sortByNameAndYear and follow the instructions
    # =============================================================================================
    # DO NOT CHNAGE
    print("\n\n=== List alphabetically only those animals that were named in 1758 ===")
    animals = sortByNameAndYear(animalsList)
    # =============================================================================================
    # on the line below, loop through the *animals* list and print each animal


# ================== Functions to solve =====================
def orderByYearNamedDesc(animalsList):
    # using the **animalsList** create a new list
    # with all the animals in descending order by year named
    # and assign the new list to **sorted_animals**
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def sortAnimalsByName(animalsList):
    # using the **animalsList** create a new list
    # with all the animals stored alphabetically
    # and assign the new list to **sorted_animals**
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def sortAnimalsByMovement(animlasList):
    # using the **animalsList** create a new list
    # with all the animals order by how they move
    # and assign the new list to **sorted_animals**
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def findAnimalsWithLungs(animalsList):
    # usint the **animalsList** create a new list
    # with only animals that breath with lungs
    # and assign the new list to **sorted_animals**
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def findByLungsAndYear(animalsList):
    # using the **animalsList** create a new list
    # with only those animals that breath with lungs and were named in 1758
    # and assign the new list to **sorted_animals**
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def findByEggsAndLungs(animalsList):
    # using the **animalsList** create a new list
    # with only those animals that lay eggs and breath with lungs
    # and assign the new list to **sorted_animals**
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def sortByNameAndYear(animalsList):
    # using the **animalsList** create a new list
    # with animals sorted alphabetically AND
    # only those animals that were named in 1758
    # assign the new list to **sorted_animals**
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


if __name__ == "__main__":
    # remove the **pass** and call the **main** function
    pass
