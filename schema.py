import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import BakeryItem as ItemModel, db

class Item(SQLAlchemyObjectType):
    class Meta:
        model = ItemModel

class Query(graphene.ObjectType):
    items = graphene.List(Item)

    def resolve_items(self, info):
        return db.session.execute(db.select(ItemModel)).scalars()
    