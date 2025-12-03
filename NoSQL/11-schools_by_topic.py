#!/usr/bin/env python3
"""
a module containing a function that search for documents with specific topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that takes a topic
    and returns all of the documents that contains it

    Attributes:
        mongo_collection: a mongo collection
        topic: a topic to search for

    Returns:
        all of the documents that contains the topic
    """
    cursor = mongo_collection.find({"topics": topic})

    result = []
    for value in cursor:
        result.append(value)

    return result
