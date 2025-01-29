class KeyValueStore:
    def __init__(self):
        self.store = {}  # Main key-value store
        self.transaction_stack = []  # Stack to track changes in a transaction

    def set(self, key, value):
        # If there's an active transaction, push the current state onto the stack
        if self.transaction_stack:
            self.transaction_stack[-1].append(('SET', key, self.store.get(key)))
        self.store[key] = value

    def get(self, key):
        return self.store.get(key, None)

    def delete(self, key):
        # If there's an active transaction, push the current state onto the stack
        if key in self.store:
            if self.transaction_stack:
                self.transaction_stack[-1].append(('DELETE', key, self.store[key]))
            del self.store[key]

    def begin_transaction(self):
        # Begin a new transaction and add a new empty stack to track changes
        self.transaction_stack.append([])

    def rollback(self):
        # Rollback the last transaction, reverting changes
        if self.transaction_stack:
            changes = self.transaction_stack.pop()
            for operation, key, old_value in reversed(changes):
                if operation == 'SET':
                    if old_value is None:
                        # If the old value was None, delete the key (rollback the SET operation)
                        self.store.pop(key, None)
                    else:
                        # Restore the old value
                        self.store[key] = old_value
                elif operation == 'DELETE':
                    # Restore the deleted key (rollback the DELETE operation)
                    self.store[key] = old_value
        else:
            print("No active transaction to rollback.")

    def commit(self):
        # Commit the last transaction (empty the transaction stack)
        if self.transaction_stack:
            self.transaction_stack.pop()
        else:
            print("No active transaction to commit.")

# Example Usage:
kv_store = KeyValueStore()

# Set initial values
kv_store.set("key1", "value1")
kv_store.set("key2", "value2")
print(kv_store.get("key1"))  # Output: value1
print(kv_store.get("key2"))  # Output: value2

# Begin a transaction
kv_store.begin_transaction()

# Modify values and delete a key inside the transaction
kv_store.set("key1", "new_value1")
kv_store.set("key3", "value3")
kv_store.delete("key2")
print(kv_store.get("key1"))  # Output: new_value1
print(kv_store.get("key2"))  # Output: None (key2 is deleted)
print(kv_store.get("key3"))  # Output: value3

# Rollback the transaction
kv_store.rollback()
print(kv_store.get("key1"))  # Output: value1 (rollback restores original value)
print(kv_store.get("key2"))  # Output: value2 (key2 is restored)
print(kv_store.get("key3"))  # Output: None (key3 was not committed)

# Begin another transaction and commit it
kv_store.begin_transaction()
kv_store.set("key2", "new_value2")
kv_store.commit()
print(kv_store.get("key2"))  # Output: new_value2 (committed)
