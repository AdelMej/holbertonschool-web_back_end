#!/usr/bin/env python3
""" a module containing a function that updates a field with a given name"""


def update_topics(mongo_collection, name, topics):
    """
    a function that updates or add topics in a mongo collection

    Attributes:
        mongo_collection: a mongo collection to update
        name(dict): the name to search for
        topics(dict): the topics to insert or update

    Returns:
        None
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
