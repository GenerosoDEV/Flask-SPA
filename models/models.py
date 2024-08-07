from firebase_admin import db

class User:
    def __init__(self, user_id, firebase_service):
        self.user = user_id
        self.firebase_service = firebase_service

    def get(self):
        ref = db.reference(f"users/{self.user}")
        if ref is None:
            raise ValueError(f"{self.user} not found.")
        return ref.get()
    
    def update(self, new_data):
        ref = db.reference(f"users/{self.user}")
        if ref is None:
            raise ValueError(f"{self.user} not found.")
        ref.set(new_data)
