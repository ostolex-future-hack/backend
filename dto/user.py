from pydantic import BaseModel


class users_to_goals(BaseModel):
    user_id: int
    goal_id: int


class User(BaseModel):
    name: str
    language_lvl: float
    chat: str


class Goal(BaseModel):
    id: int
    name: str


class Topic(BaseModel):
    name: str


class Language(BaseModel):
    language_lvl: float
