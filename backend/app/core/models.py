from pydantic import BaseModel
from typing import Optional
from enum import Enum

class LessonStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class Lesson(BaseModel):
    number: int
    title: str
    description: Optional[str] = ""
    status: LessonStatus = LessonStatus.PENDING
    gamma_url: Optional[str] = None
    gamma_id: Optional[str] = None
    error: Optional[str] = None