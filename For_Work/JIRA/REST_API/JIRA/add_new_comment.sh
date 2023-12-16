#!/bin/bash

login="LOGIN:PASSWORD"

curl -X POST \
      --url <DOMAIN_NAME>/rest/api/2/issue/REST-1/comment \
      -u $login \
      -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -H "cache-control: no-cache" \
      -d '{

       "body": "<TEXT>"

}'

