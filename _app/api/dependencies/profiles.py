from typing import Optional

from fastapi import Depends, HTTPException, Path
from starlette.status import HTTP_404_NOT_FOUND

from api.dependencies.authentication import get_current_user_authorizer
from api.dependencies.database import get_repository
from db.errors import EntityDoesNotExist
from db.repositories.profiles import ProfilesRepository
from models.domain.profiles import Profile
from models.domain.users import User
from resources import strings


async def get_profile_by_username_from_path(
    username: str = Path(..., min_length=1),
    user: Optional[User] = Depends(get_current_user_authorizer(required=False)),
    profiles_repo: ProfilesRepository = Depends(get_repository(ProfilesRepository)),
) -> Profile:
    try:
        return await profiles_repo.get_profile_by_username(
            username=username,
            requested_user=user,
        )
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=strings.USER_DOES_NOT_EXIST_ERROR,
        )
