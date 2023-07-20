from fastapi import APIRouter, Depends, HTTPException, Response, status

from schemas import Animal, AnimalCreationProperties

router = APIRouter(prefix="")

# Our "database"
ANIMALS = [Animal(id=1, name="Neelix", age=3), Animal(id=2, name="Bonnie", age=5)]


### Helper functions: ###


def _get_animals_by_name(name: str):
    animals = list(filter(lambda animal: animal.name == name, ANIMALS))
    if len(animals) > 0:
        return animals
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Animal with name {name} not found.")


def _get_animal_by_id(id: int):
    try:
        return list(filter(lambda animal: animal.id == id, ANIMALS))[0]
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Animal with id {id} not found.")


def _generate_new_id():
    return max(ANIMALS, key=lambda x: x.id).id + 1


### ENDPOINTS: ###


@router.get("/animal/", response_model=list[Animal])
def get_all_animals():
    """
    Returns all animals in the database.
    """
    return ANIMALS


@router.get("/animal/{name}", response_model=list[Animal])
def get_animals_by_name(
    name: str,
):
    """
    Returns animals by their name.
    """
    return _get_animals_by_name(name)


@router.post("/animal/", status_code=status.HTTP_201_CREATED, response_model=Animal)
def create_animal(
    animal: AnimalCreationProperties,
    id: int = Depends(_generate_new_id),
):
    """
    Create a new animal.
    """
    new_animal = Animal(id=id, **animal.dict())
    ANIMALS.append(new_animal)
    return new_animal


@router.put("/animal/{animal_id}", status_code=status.HTTP_200_OK, response_model=Animal)
def update_animal(
    animal_id: int,
    animal: AnimalCreationProperties,
):
    """
    Update an existing animal by its id.
    """
    existing_animal = _get_animal_by_id(animal_id)

    updated_animal = Animal(id=existing_animal.id, **animal.dict())
    ANIMALS[ANIMALS.index(existing_animal)] = updated_animal

    return updated_animal


# def require_user_is_admin(...):
#     ...


@router.delete("/animal/{animal_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_animal(
    animal_id: int,
    # dependencies=[Depends(require_user_is_admin)],
):
    """
    Delete an animal by its id.
    """
    existing_animal = _get_animal_by_id(animal_id)
    ANIMALS.remove(existing_animal)
