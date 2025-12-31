from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)

class Profile(Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    address = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    user = relationship("User", uselist=False)

# Bidirectional relationship models
class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    
    # Bidirectional relationship
    bio = relationship(
        "AuthorBio",
        back_populates="author",
        uselist=False,
        cascade="all, delete"
    )

class AuthorBio(Base):
    __tablename__ = "author_bios"
    
    id = Column(Integer, primary_key=True)
    biography = Column(String)
    birth_year = Column(Integer)
    country = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"), unique=True)
    
    # Bidirectional relationship
    author = relationship("Author", back_populates="bio")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    category = Column(String)