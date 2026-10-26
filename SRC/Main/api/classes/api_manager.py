from typing import Any, List

from SRC.Main.api.steps.admin_steps import AdminSteps
from SRC.Main.api.steps.user_steps import UserSteps


class ApiManager:
    def __init__(self, created_object: List[Any]):
        self.admin_steps = AdminSteps(created_object)
        self.user_steps = UserSteps(created_object)