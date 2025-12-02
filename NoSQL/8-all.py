#!/usr/bin/env python3
""" a python script that fetch all document in a collection"""


def list_all(mongo_collection):
    """
    a function that returns the content of a collection
    """
    return list(mongo_collection.find())
