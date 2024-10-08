#!/usr/bin/env python3
""" 11-schools_by_topic - Retrieve schools by topic """

from pymongo.collection import Collection
from typing import List, Dict

def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict]:
    """ Returns a list of schools with a specific topic
    
    Args:
        mongo_collection (Collection): The pymongo collection object
        topic (str): The topic to search for
        
    Returns:
        List[Dict]: A list of documents (schools) that contain the given topic
    """
    return list(mongo_collection.find({"topics": topic}))

