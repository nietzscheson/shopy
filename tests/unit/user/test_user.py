import uuid

from shopy.user.domain.user import User


def test_user():
    id = str(uuid.uuid4())

    user = User(id=id, name="The Name")
    assert user.id == id
    assert user.name == "The Name"


def test_vote_default():
    id = str(uuid.uuid4())

    assert User().id != id
