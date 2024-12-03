from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import payment_method as model
from sqlalchemy.exc import SQLAlchemyError
from .. import schemas
from ..schemas.payment_method import PaymentMethodCreate, PaymentMethodUpdate

def create(db: Session, request):
    new_item = model.PaymentMethod(
        card_num = request.card_num,
        transaction_status = request.transaction_status,
        transaction_type = request.transaction_type
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    response_data = {
        "id": new_item.id,
        "card_num": new_item.card_num,
        "transaction_status": new_item.transaction_status.value,  
        "transaction_type": new_item.transaction_type.value    
    }
    print("Raw Response Data:", response_data)  
    return response_data

def read_all(db: Session):
    try:
        result = db.query(model.PaymentMethod).all()
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return [
        {
            "id": item.id,
            "card_num": item.card_num,
            "transaction_status": item.transaction_status.value, 
            "transaction_type": item.transaction_type.value     
        }
        for item in result
    ]

def read_one(db: Session, item_id):
    try:
        item = db.query(model.PaymentMethod).filter(model.PaymentMethod.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return {
        "id": item.id,
        "card_num": item.card_num,
        "transaction_status": item.transaction_status.value,  
        "transaction_type": item.transaction_type.value  
    }     

def update(db: Session, item_id: int, request: schemas.PaymentMethodUpdate):
    item = db.query(model.PaymentMethod).filter(model.PaymentMethod.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"PaymentMethod with id {item_id} not found"
        )

    item.card_num = request.card_num
    item.transaction_status = request.transaction_status
    item.transaction_type = request.transaction_type

    try:
        db.commit()
        db.refresh(item) 
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    return {
        "id": item.id,
        "card_num": item.card_num,
        "transaction_status": item.transaction_status.value,
        "transaction_type": item.transaction_type.value
    }


def delete(db: Session, item_id):
    try:
        item = db.query(model.PaymentMethod).filter(model.PaymentMethod.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

