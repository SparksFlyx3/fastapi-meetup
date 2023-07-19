from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models
import schemas


def get_all_animals(db: Session) -> list[schemas.Animal]:
    return [schemas.Animal.from_orm(animal) for animal in db.query(models.Animal).all()]


def get_animal_by_name(name: str, db: Session) -> schemas.Animal:
    animal = db.query(models.Animal).filter(models.Animal.name == name).first()
    if animal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Animal with name {name} not found.")
    return schemas.Animal.from_orm(animal)


def create_animal(animal: schemas.Animal, db: Session) -> schemas.Animal:
    db_animal = db.query(models.Animal).filter(models.Animal.name == animal.name).first()
    if db_animal:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="An animal with this name already exists."
        )
    db_animal = models.Animal(name=animal.name, age=animal.age)
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return schemas.Animal.from_orm(db_animal)


def update_animal(animal_id: int, animal: schemas.Animal, db: Session) -> schemas.Animal:
    db_animal = db.query(models.Animal).filter_by(id=animal_id).first()
    if not db_animal:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"There is no animal with id {animal_id}.")

    try:
        for var, value in vars(animal).items():
            setattr(db_animal, var, value) if value else None
        db.commit()
        db.refresh(db_animal)

        return schemas.Animal.from_orm(db_animal)

    except IntegrityError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail=f"There is already an animal with the name {animal.name}."
        )


def delete_animal(animal_id: int, db: Session):
    deleted_count = db.query(models.Animal).filter_by(id=animal_id).delete()
    if deleted_count > 0:
        db.commit()
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"There is no animal with id {animal_id}.")
