class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.books = []
            cls._instance.members = []
        return cls._instance
