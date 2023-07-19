from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

import crud
from database import get_db
import schemas

router = APIRouter(prefix="")


@router.get("/animal/", response_model=list[schemas.Animal])
def get_all_animals(
    db: Session = Depends(get_db),
):
    """
    Returns all animals in the database.
    """
    return crud.get_all_animals(db)


@router.get("/animal/{name}", response_model=schemas.Animal)
def get_animal_by_name(
    name: str,
    db: Session = Depends(get_db),
):
    """
    Returns an animals by its name.
    """
    return crud.get_animal_by_name(name, db)


@router.post("/animal/", status_code=status.HTTP_201_CREATED, response_model=schemas.Animal)
def create_animal(
    animal: schemas.Animal,
    db: Session = Depends(get_db),
):
    """
    Create a new animal.
    """
    return crud.create_animal(animal, db)


@router.put("/animal/{animal_id}", status_code=status.HTTP_200_OK, response_model=schemas.Animal)
def update_animal(
    animal_id: int,
    animal: schemas.Animal,
    db: Session = Depends(get_db),
):
    """
    Update an existing animal by its id.
    """
    return crud.update_animal(animal_id, animal, db)


# def require_user_is_admin(...):
#     ...

@router.delete("/animal/{animal_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_animal(
    animal_id: int,
    # dependencies=[Depends(require_user_is_admin)],
    db: Session = Depends(get_db),
):
    """
    Delete an animal by id.
    """
    return crud.delete_animal(animal_id, db)
