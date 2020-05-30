import os
import dotenv
dotenv.load_dotenv()


def get_secret(key, default=None):
    return os.getenv(key, default)


def get_key_and_type(in_dict):
    for key, value in in_dict.items():
        print(key + ':', type(value).__name__)
