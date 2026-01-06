from sqlalchemy.orm import Session
import models
import schemas

def create_role(db: Session, role: schemas.RoleCreate):
    db_role = models.Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_roles(db: Session):
    return db.query(models.Role).all()

def get_role(db: Session, role_id: int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    roles = (
        db.query(models.Role)
        .filter(models.Role.id.in_(user.role_ids))
        .all()
    )
    
    db_user = models.User(name=user.name, email=user.email)
    db_user.roles = roles
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def add_role_to_user(db: Session, user_id: int, role_id: int):
    user = get_user(db, user_id)
    if not user:
        return None
    
    role = get_role(db, role_id)
    if not role:
        return "ROLE_NOT_FOUND"
    
    if role not in user.roles:
        user.roles.append(role)
        db.commit()
        db.refresh(user)
    
    return user

def remove_role_from_user(db: Session, user_id: int, role_id: int):
    user = get_user(db, user_id)
    if not user:
        return None
    
    role = get_role(db, role_id)
    if not role:
        return "ROLE_NOT_FOUND"
    
    if role in user.roles:
        user.roles.remove(role)
        db.commit()
        db.refresh(user)
    
    return user

def set_user_roles(db: Session, user_id: int, role_ids: list[int]):
    user = get_user(db, user_id)
    if not user:
        return None
    
    roles = db.query(models.Role).filter(models.Role.id.in_(role_ids)).all()
    if len(roles) != len(role_ids):
        return "SOME_ROLES_NOT_FOUND"
    
    user.roles = roles
    db.commit()
    db.refresh(user)
    
    return user

def get_users_with_role(db: Session, role_id: int):
    role = get_role(db, role_id)
    if not role:
        return None
    return role.users