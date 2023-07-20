import pydantic


class AnimalCreationProperties(pydantic.BaseModel):
    name: str
    age: int # = pydantic.Field(42, ge=1, le=100)

    # @pydantic.validator("age")
    # def _validate_age_is_odd_number(cls, age: int) -> int:
    #     if age % 2 == 0:
    #         raise ValueError("ensure the age is an odd number")
    #     return age


class Animal(AnimalCreationProperties):
    id: int


# class Cat(AnimalCreationProperties):
#     def miau(self):
#         print(f"Cat {self.name} says miau!")


# cat = Cat(name="Bonnie", age=2)
