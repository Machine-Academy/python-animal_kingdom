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

    # Step 5: loop through the list's above, and add each object created to the **animals** list
    animals = []

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

    # Step 7: Goto the function orderByYearNamedDesc and follow the instructions
    print("=== List all the animals in descending order by year named ===")
    orderByYearNamedDesc(animals)

    # Step 8:
    print("\n\n=== List all the animals alphabetically ===")
    sortAnimalsByName(animals)

    # Step 9:
    print("\n\n=== List all the animals order by how they move ===")
    sortAnimalsByMovement(animals)

    # Step 10:
    print("\n\n=== List only those animals the breath with lungs ===")
    findAnimalsWithLungs(animals)

    # Step 11:
    print(
        "\n\n=== List only those animals that breath with lungs and were named in 1758 ==="
    )
    findByLungsAndYear(animals)

    # Step 12:
    print("\n\n=== List only those animals that lay eggs and breath with lungs ===")
    findByEggsAndLungs(animals)

    # Step 13:
    print("\n\n=== List alphabetically only those animals that were named in 1758 ===")
    sortByNameAndYear(animals)


def orderByYearNamedDesc(animalsList):
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def sortAnimalsByName(animalsList):
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def sortAnimalsByMovement(animlasList):
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def findAnimalsWithLungs(animalsList):
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def findByLungsAndYear(animalsList):
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def findByEggsAndLungs(animalsList):
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


def sortByNameAndYear(animalsList):
    sorted_animals = None

    # =====================================
    # Leave this here for the test cases
    return sorted_animals
    # =====================================


if __name__ == "__main__":
    # remove pass and call the **main** function
    pass
