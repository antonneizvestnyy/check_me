#!/bin/bash

login="LOGIN:PASSWORD"

curl -X POST \
       "<DOMAIN_NAME>/rest/api/2/issue" \
        --user $login \
        -H "Content-Type: application/json" \
        -H "cache-control: no-cache" \
        -d '{
            "fields": 
            {
               "project":
               {
                   "key": "<YOUR KEY>"
               },
               "parent":
               {
                   "key": "YOUR KEY PARENT"
               },
               "summary": "create sub-task",
               "description": "test rest api create sub-task",
               "issuetype":
               {
                   "id": "10003"
               }
            }
        }'
