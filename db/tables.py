from typing import List, TypeVar

from sqlalchemy import String, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


SQLEntity = TypeVar('SQLEntity', bound=Base)


class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    def __repr__(self):
        return f"Locations(id={self.id!r}, loc_name={self.name!r})"

    def __str__(self):
        return f"{self.id}. {self.name}"


class Weather(Base):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    def __repr__(self):
        return f"Weather(id={self.id!r}, weather_name={self.name!r})"

    def __str__(self):
        return f"{self.id}. {self.name}"


class Encounter(Base):
    __tablename__ = "encounter"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    link: Mapped[str] = mapped_column(String(255), nullable=False)
    time: Mapped[int] = mapped_column(nullable=False)
    locations: Mapped[List[int]] = mapped_column(ARRAY(Integer), nullable=False)
    weather: Mapped[List[int]] = mapped_column(ARRAY(Integer), nullable=False)
    done: Mapped[bool] = mapped_column(nullable=False)
    prerequisites: Mapped[str] = mapped_column(String(255), nullable=True)

    def __repr__(self):
        return (f"Encounters(id={self.id!r}, enc_name={self.name!r}, link={self.link!r}, time={self.time!r},"
                f" locations={self.locations!r}, weather={self.weather!r}, done={self.done!r},"
                f" prerequisites={self.prerequisites!r})")

    def __str__(self):

        return (f"\n{self.id}. {self.name}. Link: {self.link if self.link != '' else 'None'}."
                f"\nLocations: {self.locations}; Weather: {self.weather}; Time: {self.time};"
                f"\nDone: {self.done}; Prerequisites: {self.prerequisites}"
                f"\n{'=' * 45}")




