from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import menu as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    ingredients_str = ', '.join(request.ingredients) if request.ingredients else ''

    new_item = model.MenuItem(
        dish_name=request.dish_name,
        ingredients=ingredients_str,
        price=request.price,
        calories=request.calories,
        food_category=request.food_category
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        new_item.ingredients = new_item.ingredients.split(', ') if new_item.ingredients else []
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.MenuItem).all()
        for item in result:
            item.ingredients = item.ingredients.split(', ') if item.ingredients else []
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.ingredients = item.ingredients.split(', ') if item.ingredients else []
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        update_data = request.dict(exclude_unset=True)
        if 'ingredients' in update_data and update_data['ingredients']:
            update_data['ingredients'] = ', '.join(update_data['ingredients'])

        item.update(update_data, synchronize_session=False)
        db.commit()

        updated_item = item.first()
        updated_item.ingredients = updated_item.ingredients.split(', ') if updated_item.ingredients else []
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return updated_item


def delete(db: Session, item_id):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)