class KeyValueStore:
    """
    Nested Transaction Commits: Any changes made by nested transactions are considered provisional.

    Outer Transaction Rollbacks: If the outer transaction is rolled back, those provisional changes from nested transactions are undone as well.
    """
    def __init__(self):
        self.store = {}
        # Event Sourcing
        self.transactions = []

    def __str__(self):
        return str(self.store)

    def set(self, key, value):
        if self.transactions:
            self.transactions[-1].append(('SET', key, self.store.get(key)))
        self.store[key] = value

    def delete(self, key):
        if key in self.store:
            if self.transactions:
                self.transactions[-1].append(('DEL', key, self.store.get(key)))

            del self.store[key]

    def begin_trans(self):
        # stack of stack to support nested trans
        self.transactions.append([])

    def rollback(self):
        if self.transactions:
            events = self.transactions.pop()
            for operation, key, value in reversed(events):
                if operation == 'SET':
                    if value is None:
                        del self.store[key]
                    else:
                        self.store[key] = value
                elif operation == 'DEL':
                    self.store[key] = value

    def commit(self):
        if self.transactions:
            self.transactions.pop()


kv = KeyValueStore()
# kv.set('A', 1)  # Original value is 1
# print(kv)  # Output: {'A': 1}
#
# kv.begin_trans()
# kv.set('A', 2)  # Set A to 2 within the first transaction
# kv.begin_trans()
# kv.set('A', 3)  # Set A to 3 within the nested transaction
# kv.rollback()  # Rollback the nested transaction, reverting A to 2
# print(kv)  # Output: {'A': 2}
#
# kv.commit()  # Commit the outer transaction
# print(kv)  # Output: {'A': 2}


kv.begin_trans()
kv.set('A', 4)  # Set A to 2 within the first transaction
kv.begin_trans()
kv.set('A', 5)  # Set A to 3 within the nested transaction
kv.commit()  # Rollback the nested transaction, reverting A to 2
print(kv)

kv.rollback()  # Commit the outer transaction
print(kv)