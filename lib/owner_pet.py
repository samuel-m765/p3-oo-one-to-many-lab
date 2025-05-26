class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return all pets that belong to this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Check pet is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")
        # Set this owner as the pet's owner
        pet.owner = self

    def get_sorted_pets(self):
        # Return the owner's pets sorted by name
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}. Must be one of {Pet.PET_TYPES}")

        self.name = name
        self.pet_type = pet_type

        # owner is optional, if given, must be an Owner instance
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an Owner instance or None")
        self.owner = owner

        # Add this pet instance to the all list
        Pet.all.append(self)
