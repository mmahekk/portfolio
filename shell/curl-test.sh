#!/bin/bash

# Create a timeline post
curl -X POST http://localhost:5000/api/timeline_post -d 'date=July 2023&title=Summer U1&events=MLH Fellowship'

# Fetch timeline posts
curl http://localhost:5000/api/timeline_post

# Delete a timeline post
curl -X DELETE http://localhost:5000/api/timeline_post -d 'id=1'
