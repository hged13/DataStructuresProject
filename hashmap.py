#creates hashmap class

class HashMap:

    # creates the hashmap
    # sets size to 40
    # sets empty individual arrays
    #Space-Time complexity: 40n + 1 = O(n)
    def __init__(self, start_size=40):
        self.array = []
        for i in range(start_size):
            self.array.append([])

    # returns the bucket that the key is in
    # sets hash to formula to store the keys
    #space time complexity: O(1)
    def _get_hash(self, key):
        bucket = int(key) % len(self.array)
        return bucket

    # adds an element to the hash table
    #space time complexity: O(1)
    def insert(self, key, item):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]

        bucket_list.append(item)

    # returns the value in the bucket, using the key
    #space time complexity: O(1)
    def get(self, key):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]
        # search for key
        if int(bucket_list[0][0]) == key:
            return (bucket_list)
        # else:

    #     return None
    #returns the address of the package
    #Space time complexity: O(1)
    def getaddress(self, key):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]
        # search for key
        if int(bucket_list[0][0]) == key:
            return (bucket_list[0][1])
    #updates the package address
    #space time complexity: O(1)

    def updateaddress(self, key, address):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]

        if int(bucket_list[0][0]) == key:
            bucket_list[0][1] = address
            return bucket_list[0][1]
    #updates the city
    #space time complexity: O(1)

    def updatecity(self, key, city):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]

        if int(bucket_list[0][0]) == key:
            bucket_list[0][2] = city
            return bucket_list[0][2]
    #updates the state
    #space time complexity: O(1)

    def updatestate(self, key, state):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]

        if int(bucket_list[0][0]) == key:
            bucket_list[0][3] = state
            return bucket_list[0][3]
    #updates the zip
    #space time complexity: O(1)

    def updatezip(self, key, zip):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]

        if int(bucket_list[0][0]) == key:
            bucket_list[0][4] = zip
            return bucket_list[0][4]
    #adds a timestamp
    #space time complexity: O(1)

    def addtimestamp(self, key, timestamp):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]

        if int(bucket_list[0][0]) == key:
            bucket_list[0][9] = timestamp


    #returns the timestamp
    #space time complexity: O(1)

    def gettimestamp(self, key):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]
        # search for key
        if int(bucket_list[0][0]) == key:
            return bucket_list[0][9]

        # returns the timestamp
        # space time complexity: O(1)

    def getstatus(self, key):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]
        # search for key
        if int(bucket_list[0][0]) == key:
            return bucket_list[0][8]

    #update status
    #space time complexity: O(1)

    def updatestatus(self, key, status):
        bucket = int(key) % len(self.array)
        bucket_list = self.array[bucket]

        if int(bucket_list[0][0]) == key:
            bucket_list[0][8] = status
            return bucket_list[0][8]


    # print the hash table
    #space time complexity: O(N)

    def print(self):

        for item in self.array:
            if item is not None:
                print(str(item))
