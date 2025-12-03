#!/usr/bin/env python3
""" a module containing a function that insert item into mango db school collection"""


def insert_school(mongo_collection, **kwargs):
    """
    function that insert elements in a collection

    Attribute:
        mango_collection: the collection to insert into

    Returns:
        the id of the newly inserted item
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
