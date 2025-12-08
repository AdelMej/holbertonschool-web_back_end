#!/usr/bin/env python3
""" a file containing a python script that output stats about nginx dump"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    main entry point for my log watching script
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    logs_collection = client.logs.nginx

    print("{} logs".format(logs_collection.count_documents({})))
    print("Methods:")
    print(
        "\tmethod GET: {}"
        .format(logs_collection.count_documents({"method": "GET"}))
    )
    print(
        "\tmethod POST: {}"
        .format(logs_collection.count_documents({"method": "POST"}))
    )
    print(
        "\tmethod PUT: {}"
        .format(logs_collection.count_documents({"method": "PUT"}))
    )
    print(
        "\tmethod PATCH: {}"
        .format(logs_collection.count_documents({"method": "PATCH"}))
    )
    print(
        "\tmethod DELETE: {}"
        .format(logs_collection.count_documents({"method": "DELETE"}))
    )
    print(
        "{} status check"
        .format(
            logs_collection.count_documents(
                {
                    "method": "GET",
                    "path": "/status"
                }
            )
        )
    )
