from sqlalchemy.orm import Session
import models
import schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(models.Product).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.category = product.category
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product

# Profile CRUD operations
def create_profile(db: Session, profile: schemas.ProfileCreate, user_id: int):
    db_profile = models.Profile(
        age=profile.age,
        address=profile.address,
        user_id=user_id
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_profile_by_user_id(db: Session, user_id: int):
    return db.query(models.Profile).filter(models.Profile.user_id == user_id).first()

def update_profile(db: Session, user_id: int, profile: schemas.ProfileCreate):
    db_profile = get_profile_by_user_id(db, user_id)
    if not db_profile:
        return None
    
    db_profile.age = profile.age
    db_profile.address = profile.address
    db.commit()
    db.refresh(db_profile)
    return db_profile

def delete_profile(db: Session, user_id: int):
    db_profile = get_profile_by_user_id(db, user_id)
    if not db_profile:
        return None
    db.delete(db_profile)
    db.commit()
    return db_profile

# Bidirectional CRUD operations (Author <-> AuthorBio)
def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(
        name=author.name,
        email=author.email
    )
    
    if author.bio:
        db_bio = models.AuthorBio(
            biography=author.bio.biography,
            birth_year=author.bio.birth_year,
            country=author.bio.country
        )
        db_author.bio = db_bio
    
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session):
    return db.query(models.Author).all()

def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def update_author(db: Session, author_id: int, author: schemas.AuthorUpdate):
    db_author = get_author(db, author_id)
    if not db_author:
        return None
    db_author.name = author.name
    db_author.email = author.email
    db.commit()
    db.refresh(db_author)
    return db_author

def delete_author(db: Session, author_id: int):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        return None
    db.delete(author)
    db.commit()
    return author

# AuthorBio CRUD operations
def create_author_bio(db: Session, bio: schemas.AuthorBioCreate, author_id: int):
    db_bio = models.AuthorBio(
        biography=bio.biography,
        birth_year=bio.birth_year,
        country=bio.country,
        author_id=author_id
    )
    db.add(db_bio)
    db.commit()
    db.refresh(db_bio)
    return db_bio

def get_author_bio_by_author_id(db: Session, author_id: int):
    return db.query(models.AuthorBio).filter(models.AuthorBio.author_id == author_id).first()

def update_author_bio(db: Session, author_id: int, bio: schemas.AuthorBioCreate):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        return None
    
    if author.bio:
        author.bio.biography = bio.biography
        author.bio.birth_year = bio.birth_year
        author.bio.country = bio.country
    else:
        author.bio = models.AuthorBio(
            biography=bio.biography,
            birth_year=bio.birth_year,
            country=bio.country
        )
    
    db.commit()
    db.refresh(author)
    return author

def delete_author_bio(db: Session, author_id: int):
    db_bio = get_author_bio_by_author_id(db, author_id)
    if not db_bio:
        return None
    db.delete(db_bio)
    db.commit()
    return db_bio