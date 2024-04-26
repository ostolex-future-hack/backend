from models.user import User, Goal, users_to_goals, Language
from sqlalchemy.orm import Session
from dto import user


def create_user(data: user.User, db: Session):
    user = User(name=data.name)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as er:
        print(er)
    return user


def update_user_language_lvl(id: int, data: user.User, db: Session):
    user = db.query(User).filter(User.id == id).first()
    user.language_lvl = data.language_lvl

    db.add(user)
    db.commit()
    return user


def get_user(id: int, db):
    return db.query(User).filter(User.id == id).first()


def update(data: user.User, db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    user.name = data.name

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def remove(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return user


def create_goal_s(data: user.Goal, db: Session):
    goal = Goal(name=data.name)
    try:
        db.add(goal)
        db.commit()
        db.refresh(goal)
    except Exception as er:
        print(er)
    return goal


def get_goal_s(db: Session, id: int):
    return db.query(Goal).filter(Goal.id == id).first()


def add_goals_to_user(data: user.users_to_goals, db: Session):
    user = get_user(data.user_id, db)
    goal = get_goal_s(db, data.goal_id)
    try:
        user.goals.append(goal)
        db.commit()

    except Exception as er:
        print(er)
    return user


def get_users_to_goal_s(user_id: int, db: Session):
    # return db.query(users_to_goals).filter_by(user_id=user_id).all()
    user_obj = get_user(user_id, db)
    return user_obj.goals


def create_language_lvl(data: user.Language, db: Session):
    language = Language(language_lvl=data.language_lvl)
    try:
        db.add(language)
        db.commit()
        db.refresh(language)
    except Exception as er:
        print(er)
    return language


def get_language_lvl(db: Session, lang: float):
    return db.query(Language).filter(Language.language_lvl == lang).first()
