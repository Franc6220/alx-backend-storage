def top_students(mongo_collection):
    # Calculate the average score for each student and sort by average score
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$divide": [
                        {"$sum": "$topics.score"},
                        {"$size": "$topics"}
                    ]
                }
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    # Aggregate the results
    students = list(mongo_collection.aggregate(pipeline))

    # Format the output
    for student in students:
        student['averageScore'] = float(student['averageScore'])
    
    return students

