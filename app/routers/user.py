"""USER Router"""

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ..database import get_session
from ..models.user import User
from ..auth.auth_methods import get_current_active_user

session = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@router.get("/me/items")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]


@router.get("/{user_id}", response_model=User)
def get_user_by_id(user_id: int, session: session):
    """Get a single user by id

    Args:
        user_id (int): The user id to query
        session (Annotated[Session, Depends): Session object for the transaction

    Raises:
        HTTPException: 404 if user not found

    Returns:
        user: User found by id
    """
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
