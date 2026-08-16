class ContactBook:
    def __init__(self, path='contacts.json'):
        self.path = path
        try:
            with open(path) as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            self.contacts = []

    def add(self, name, phone):
        self.contacts.append(
            {"name": name, "phone": phone})
        self.save()

    def search(self, term):
        return [c for c in self.contacts
                if term.lower() in c["name"].lower()]
