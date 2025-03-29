from sqlalchemy.orm import Session
from app.models import Notification
from app.schemas import NotificationCreate, NotificationUpdate

def get_notification(db: Session, notification_id: str):
    return db.query(Notification).filter(Notification.id == notification_id).first()

def get_notifications(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Notification).offset(skip).limit(limit).all()

def create_notification(db: Session, notification: NotificationCreate):
    db_notification = Notification(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

def update_notification(db: Session, notification_id: str, notification: NotificationUpdate):
    db_notification = get_notification(db, notification_id)
    if db_notification:
        update_data = notification.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_notification, key, value)
        db.commit()
        db.refresh(db_notification)
        return db_notification
    return None