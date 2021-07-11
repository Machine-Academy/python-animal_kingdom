# Project Animal Kingdom Basic

A student that completes this project shows that they can:

* Use and implement Classes
* Use and understand Lambdas
* Use and understand List Comprehension
* Use and understand `sorted`
## Introduction

Using a combination of classes, lambda expressions and List Comprehension you will create and manipulate a list of animals.

## Instruction

* [ ] Please fork and clone this repository. Regularly commit and push your code as appropriate.
* [ ] Create an base class to be used for all animals
  * [ ] Each animal is assigned a name, and year discovered regardless of classification.
  * [ ] Each animal should have a method that returns the assigned name and year discovered.

- [ ] Methods will return a string saying how that animal implements the action
  - [ ] All animals can move, breath, reproduce. How they do that, so what string should get returned when the method is executed, varies by animal type.

* [ ] Create classes for mammals, birds, fish
  * [ ] Mammals move - walk, breath - lungs, reproduce - live births
  * [ ] Birds move - fly, breath - lungs, reproduce - eggs
  * [ ] Fish move - swim, breath - gills, reproduce - eggs

Create a collection for ALL the animals using the following data

* [ ] **Mammals:**

    | Name      | Year Named |
    |-----------|-------|
    | Panda     | 1869  |
    | Zebra     | 1778  |
    | Koala     | 1816  |
    | Sloth     | 1804  |
    | Armadillo | 1758  |
    | Raccoon   | 1758  |
    | Bigfoot   | 2021  |

* [ ] **Birds:**

    | Name      | Year Named |
    |-----------|------|
    | Pigeon    | 1837 |
    | Peacock   | 1821 |
    | Toucan    | 1758 |
    | Parrot    | 1824 |
    | Swan      | 1758 |

* [ ] **Fish:**

    | Name      | Year Named |
    |-----------|------|
    | Salmon    | 1758 |
    | Catfish   | 1817 |
    | Perch     | 1758 |

* Using Pythons `sort` display the results to the console
  * [ ] List all the animals in descending order by year named
  * [ ] List all the animals alphabetically
  * [ ] List all the animals order by how they move

* Using List Comprehensions display the results to the console
  * [ ] List only those animals the breath with lungs
  * [ ] List only those animals that breath with lungs and were named in 1758
  * [ ] List only those animals that lay eggs and breath with lungs

* Using a Lambda AND List Comprehensions display the result to the console  
  * [ ] List alphabetically only those animals that were named in 1758

* Stretch Goal
  * [ ] For the list of animals, list alphabetically those animals that are mammals.

## Results

### MVP

The MVP of this application would produce the following output

```TEXT
=== List all the animals in descending order by year named ===
{ name: BigFoot, year_discovered: 2021 }
{ name: Panda, year_discovered: 1869 }
{ name: Pigeon, year_discovered: 1837 }
{ name: Parrot, year_discovered: 1824 }
{ name: Peacock, year_discovered: 1821 }
{ name: Catfish, year_discovered: 1817 }
{ name: Koala, year_discovered: 1816 }
{ name: Sloth, year_discovered: 1804 }
{ name: Zebra, year_discovered: 1778 }
{ name: Armadillo, year_discovered: 1758 }
{ name: Raccoon, year_discovered: 1758 }
{ name: Toucan, year_discovered: 1758 }
{ name: Swan, year_discovered: 1758 }
{ name: Salmon, year_discovered: 1758 }
{ name: Perch, year_discovered: 1758 }


=== List all the animals alphabetically ===
{ name: Armadillo }
{ name: BigFoot }
{ name: Catfish }
{ name: Koala }
{ name: Panda }
{ name: Parrot }
{ name: Peacock }
{ name: Perch }
{ name: Pigeon }
{ name: Raccoon }
{ name: Salmon }
{ name: Sloth }
{ name: Swan }
{ name: Toucan }
{ name: Zebra }


=== List all the animals order by how they move ===
{ name: Pigeon, move: fly }
{ name: Peacock, move: fly }
{ name: Toucan, move: fly }
{ name: Parrot, move: fly }
{ name: Swan, move: fly }
{ name: Salmon, move: swim }
{ name: Catfish, move: swim }
{ name: Perch, move: swim }
{ name: Panda, move: walk }
{ name: Zebra, move: walk }
{ name: Koala, move: walk }
{ name: Sloth, move: walk }
{ name: Armadillo, move: walk }
{ name: Raccoon, move: walk }
{ name: BigFoot, move: walk }


=== List only those animals the breath with lungs ===
{ name: Panda, breathe: lungs }
{ name: Zebra, breathe: lungs }
{ name: Koala, breathe: lungs }
{ name: Sloth, breathe: lungs }
{ name: Armadillo, breathe: lungs }
{ name: Raccoon, breathe: lungs }
{ name: BigFoot, breathe: lungs }
{ name: Pigeon, breathe: lungs }
{ name: Peacock, breathe: lungs }
{ name: Toucan, breathe: lungs }
{ name: Parrot, breathe: lungs }
{ name: Swan, breathe: lungs }


=== List only those animals that breath with lungs and were named in 1758 ===
{ name: Armadillo, breathe: lungs, year_discovered: 1758 }
{ name: Raccoon, breathe: lungs, year_discovered: 1758 }
{ name: Toucan, breathe: lungs, year_discovered: 1758 }
{ name: Swan, breathe: lungs, year_discovered: 1758 }


=== List only those animals that lay eggs and breath with lungs ===
{ name: Pigeon, breathes: lungs, reproduces: eggs }
{ name: Peacock, breathes: lungs, reproduces: eggs }
{ name: Toucan, breathes: lungs, reproduces: eggs }
{ name: Parrot, breathes: lungs, reproduces: eggs }
{ name: Swan, breathes: lungs, reproduces: eggs }


=== List alphabetically only those animals that were named in 1758 ===
{ name: Armadillo, year_discovered: 1758 }
{ name: Perch, year_discovered: 1758 }
{ name: Raccoon, year_discovered: 1758 }
{ name: Salmon, year_discovered: 1758 }
{ name: Swan, year_discovered: 1758 }
{ name: Toucan, year_discovered: 1758 }
```

### Stretch Goal

The Stretch Goals would produce the following output.

```TEXT
*** Stretch Goal ***

*** For the list of animals, list alphabetically those animals that are mammals ***
Armadillo live births walk lungs 1758
Bigfoot live births walk lungs 2021
Koala live births walk lungs 1816
Panda live births walk lungs 1869
Raccoon live births walk lungs 1758
Sloth live births walk lungs 1804
Zebra live births walk lungs 1778
```
