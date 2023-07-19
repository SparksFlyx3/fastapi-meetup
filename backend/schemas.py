import pydantic


class Animal(pydantic.BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True


# class Cat(Animal):
#     def miau(self):
#         print(f"Cat {self.name} says miau!")

#     class Config:
#         orm_mode = True


# cat = Cat(name="Bonnie", age=2)
