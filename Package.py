# package class for adding the packages to the hashmap
class Package:
    #Space time complexity: O(1)
    def _init_(self, id, address, city, state, zip, deadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

