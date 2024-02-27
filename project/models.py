from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    status = Column(Boolean, default=False)

    def as_dict(self):
        return {"id": self.id, "name": self.name, "status": 1 if self.status else 0}
