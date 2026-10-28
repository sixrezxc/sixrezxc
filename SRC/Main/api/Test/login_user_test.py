import pytest

from sqlalchemy.orm import Session
from SRC.Main.api.classes.api_manager import ApiManager
from SRC.Main.api.db.crud.user_crud import UserCrudDb as User
from SRC.Main.api.models.create_user_request import CreateUserRequest

@pytest.mark.api
class TestUserLogin:
    def test_login_user(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):
        response = api_manager.admin_steps.login_user(create_user_request)

        assert create_user_request.username == response.user.username
        assert response.user.role == "ROLE_USER"
        user_from_db = User.get_user_be_username(db_session, create_user_request.username)
        assert user_from_db is not None
        assert user_from_db.username == create_user_request.username, 'Имя пользователя не совподает с базой данных'
