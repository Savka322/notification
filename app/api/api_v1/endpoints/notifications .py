from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Notification)
def create_notification(
    notification_in: schemas.NotificationCreate, db: Session = Depends(get_db)
):
    return crud.create_notification(db=db, notification=notification_in)

@router.get("/", response_model=list[schemas.Notification])
def read_notifications(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notifications = crud.get_notifications(db, skip=skip, limit=limit)
    return notifications

@router.get("/{notification_id}", response_model=schemas.Notification)
def read_notification(notification_id: str, db: Session = Depends(get_db)):
    notification = crud.get_notification(db, notification_id=notification_id)
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

@router.patch("/{notification_id}", response_model=schemas.Notification)
def update_notification(
    notification_id: str,
    notification_in: schemas.NotificationUpdate,
    db: Session = Depends(get_db),
):
    notification = crud.update_notification(
        db=db, notification_id=notification_id, notification=notification_in
    )
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification