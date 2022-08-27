from tests.demo_project_provider.src.entities.People.People import People


class TUser(People):
    def __init__(self, name, age, phone, id_card):
        super().__init__(name, age)
        self.phone = phone
        self.id_card = id_card

    def __data__(self):
        return {
            'name': self.name,
            'age': self.age,
            'phone': self.phone,
            'id_card': self.id_card
        }
