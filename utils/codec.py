import bcrypt


class Codec:
    def encode(password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def compare(password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
