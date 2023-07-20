import pydantic


class AnimalCreationProperties(pydantic.BaseModel):
    name: str
    age: int  # = pydantic.Field(ge=1, le=100)

    # @pydantic.validator("age")
    # def _validate_age_is_odd_number(cls, age: int) -> int:
    #     if age % 2 == 0:
    #         raise ValueError("ensure the age is an odd number")
    #     return age


class Animal(AnimalCreationProperties):
    id: int


# Our "database"
ANIMALS = [Animal(id=1, name="Neelix", age=3), Animal(id=2, name="Bonnie", age=5)]
