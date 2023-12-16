#!/bin/bash

#минимальный набор настроек при создании
#при создании задачи исполнитель - ЛИД

login="LOGIN:PASSWORD"

curl -X POST \
       "<DOMAIN_NAME>/rest/api/2/project" \
        --user $login \
        -H "Content-Type: application/json" \
        -H "cache-control: no-cache" \
        -d '{
  "key": "<KEY>",
  "name": "<NAME>",
  "projectTypeKey": "software",
  "description": "REST API",
  "lead": "<USER>",
  "assigneeType": "PROJECT_LEAD", 
  "avatarId": 10200
}'

