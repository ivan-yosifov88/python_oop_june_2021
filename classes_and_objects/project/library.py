class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"

        self.user_records.remove(user)
        if user in self.rented_books:
            self.rented_books.pop(user)

    def change_username(self, user_id, new_username):
        filtered_user = [user for user in self.user_records if user.user_id == user_id]

        if not filtered_user:
            return f"There is no user with id = {user_id}!"

        current_user = filtered_user[0]

        if current_user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        if current_user.username in self.rented_books:
            self.rented_books[new_username] = self.rented_books[current_user.username]
            del self.rented_books[current_user.username]
        for user in self.user_records:
            if user.username == current_user.username:
                user.username = new_username
                break
        return f"Username successfully changed to: {new_username} for userid: {user_id}"
