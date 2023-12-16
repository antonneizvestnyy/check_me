#!/bin/bash

login="LOGIN:PASSWORD"

curl -X PUT \
      --url "<DOMAIN_NAME>/rest/api/2/issue/<ISSUE_KEY>/assignee" \
      -u $login \
      -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -d '{
   "name": "<USER>"
}'
