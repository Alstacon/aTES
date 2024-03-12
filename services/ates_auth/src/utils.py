import uuid


def get_public_id() -> str:
    return uuid.uuid4().hex
