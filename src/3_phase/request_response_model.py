from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class ItemResponse(BaseModel):
    name: str
    price_with_tax: float


items: list[Item] = [
    Item(name='PlayStation 5', price=10.0),
    Item(name='Xbox Series X', price=70.0, tax=0.2),
    Item(name='Nintendo Switch', price=60.0, tax=0.1)
]


def calculate_price_with_tax(price: float, tax: float | None = None) -> float:
    price_with_tax = price * (1 + (tax or 0))
    return price_with_tax.__round__(0)


@app.post('/items', response_model=ItemResponse)
async def create_item(item: Item):
    """
    Define route for POST request to the path '/items'
    """
    price_with_tax = calculate_price_with_tax(item.price, item.tax)
    items.append(item)
    return ItemResponse(name=item.name, price_with_tax=price_with_tax)


@app.get('/items')
async def get_items() -> list[ItemResponse]:
    """
    Define route for GET request to the path '/items'
    """
    return [ItemResponse(name=item.name, price_with_tax=calculate_price_with_tax(item.price, item.tax)) for item in items]
