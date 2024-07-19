from sqlmodel import SQLModel, Field, Column, JSON
import sqlalchemy.dialects.mysql as mysql
from datetime import datetime
from typing import Dict, Any


# each class represent new table
class ModelName(SQLModel, table=True):
    __tablename__ = 'table_name'

    # your fields
