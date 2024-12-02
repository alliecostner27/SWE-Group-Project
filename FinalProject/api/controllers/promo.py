from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import promo as model
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


def create(db: Session, request):
    # Check for existing promo with the same code
    existing_promo = db.query(model.Promo).filter(model.Promo.code == request.code).first()
    if existing_promo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Promo code already exists.")

    new_item = model.Promo(
        id=request.id,
        code=request.code,
        expiration_date=request.expiration_date
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except IntegrityError:
        db.rollback()  # Rollback session in case of an integrity error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Duplicate entry for promo code.")
    except SQLAlchemyError as e:
        db.rollback()  # Rollback session for other SQL errors
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Promo).all()
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Promo).filter(model.Promo.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Promo).filter(model.Promo.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Promo).filter(model.Promo.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return Response(status_code=status.HTTP_204_NO_CONTENT)