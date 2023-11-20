from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass

class UserExistsError(Exception):
    pass

class UsernameTooShortError(Exception):
    pass

class UsernameNotLetterError(Exception):
    pass

class PasswordTooShortError(Exception):
    pass

class PasswordContaininOnlyLetters(Exception):
    pass

class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        users = self._user_repository.find_all()

        usernames = [i.username for i in users]
        if username in usernames:
            raise UserExistsError("Username already exists")
        
        if len(username) < 3:
            raise UsernameTooShortError("Username has to be 3 or more letters")

        if not re.match("^[a-z]+$", username):
            raise UsernameNotLetterError("Username must contain only letters a-z")
        
        if len(password) < 8:
            raise PasswordTooShortError("Password needs to be more than 7 characters long")
        
        if re.match("^[a-z]+$", password):
            raise PasswordContaininOnlyLetters("Password has to contain something else than just letters")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
