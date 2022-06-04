import bcrypt


class Codec:
    def encode(password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
