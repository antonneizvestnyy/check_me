#!/bin/bash

curl -X POST \
        --url "<DOMAIN_NAME>/rest/api/2/issue" \
        -u $login \
        -H "Content-Type: application/json" \
        -H "cache-control: no-cache" \
        -d '{
            "fields": {
               "project":
               {
                   "key": "<NAME_KEY>"
               },
               "summary": "<NAME_SUMMARY>",
               "description": "rest api create issue",
               "issuetype": {
               "name": "Task"
                }
            }    
        }'
