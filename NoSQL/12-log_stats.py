#!/usr/bin/env python3
""" a file containing a python script that output stats about nginx dump"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    main entry point for my log watching script
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    logs_collection = client.logs.nginx

    print(str(logs_collection.count_documents({})) + " logs")
    print("Methods:")
    print(
        "\tmethod GET: " +
        str(logs_collection.count_documents({"method": "GET"}))
    )
    print(
        "\tmethod POST: " +
        str(logs_collection.count_documents({"method": "POST"}))
    )
    print(
        "\tmethod PUT: " +
        str(logs_collection.count_documents({"method": "PUT"}))
    )
    print(
        "\tmethod PATCH: " +
        str(logs_collection.count_documents({"method": "PATCH"}))
    )
    print(
        "\tmethod DELETE: " +
        str(logs_collection.count_documents({"method": "DELETE"}))
    )
    print(
        str(
            logs_collection.count_documents(
                {
                    "method": "GET",
                    "path": "/status"
                }
            )
        ) +
        " status check"
    )
