#!/usr/bin/env python3
""" 9-insert_school - Insert a new document into a collection """

from pymongo.collection import Collection
from typing import Any

def insert_school(mongo_collection: Collection, **kwargs: Any) -> str:
    """ Inserts a new document into the collection based on kwargs
    
    Args:
        mongo_collection (Collection): The pymongo collection object
        **kwargs (Any): Document fields and their values
    
    Returns:
        str: The _id of the newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)

