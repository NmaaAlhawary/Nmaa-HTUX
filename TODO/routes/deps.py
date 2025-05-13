# import logging
# from typing import Annotated, Type
#
# from fastapi import Depends, HTTPException
# from pydantic import ValidationError
#
# from sqlalchemy.orm import Session
# from starlette import status
#
# from DB import get_async_db
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
#
# SessionDep = Annotated[Session, Depends(get_async_db)]
# routes/deps.py

from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from DB.database import get_async_db

SessionDep = Annotated[AsyncSession, Depends(get_async_db)]
