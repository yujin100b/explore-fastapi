from typing import Optional

from models.domain.rwmodel import RWModel


class Profile(RWModel):
    username: str
    bio: str = ""
    image: Optional[str] = None
    following: bool = False
