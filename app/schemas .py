from pydantic import BaseModel, UUID4, Field
from typing import Optional
from datetime import datetime

class NotificationBase(BaseModel):
    user_id: UUID4
    title: str
    text: str

class NotificationCreate(NotificationBase):
    pass

class NotificationUpdate(BaseModel):
    read_at: Optional[datetime] = None

class NotificationInDBBase(NotificationBase):
    id: UUID4
    created_at: datetime
    read_at: Optional[datetime] = None
    category: Optional[str] = None
    confidence: Optional[float] = None
    processing_status: str

    class Config:
        orm_mode = True

class Notification(NotificationInDBBase):
    pass