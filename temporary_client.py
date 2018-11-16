from secrets import randbelow


class Client:
    """
    Client class for testing purposes.
    Client creates private_key on initialization to be used when calculating a new shared_secret key.
    """
    def __init__(self):
        # Create random secret key for temporary client to use (below ten-thousand).
        # Scaling?
        self.private_key = randbelow(100)
        self.shared_secret = -1

    def calculate_key(self, generator, prime):
        self.shared_secret = (generator ** self.private_key) % prime
        return self.shared_secret


if __name__ == '__main__':
    test = Client()
    print(test.private_key)
    print(test.calculate_key(2, 11))
