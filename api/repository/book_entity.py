from sqlalchemy import Column, Integer, String
from api.repository import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement='auto')
    name = Column(String, index=True)
    author = Column(String, index=True)
    description = Column(String)

    def __init__(self, name, author, description) -> None:
        self.name = name
        self.author = author
        self.description = description

    def __repr__(self) -> str:
        return 'Book[id: {}, name: {}, author: {}, description: {}]'.format(self.id, self.name, self.author,
                                                                            self.description)

    def serialize(self) -> str:
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'description': self.description
        }
