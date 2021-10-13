# Address class for accessing column of distance data
class Address:
    #space time complexity: O(1)
    def __init__(self, address, row):
        self.address = address
        self.row = row

    #space time complexity: O(1)
    def lookupaddress(self):
        return self.row
