#!/bin/bash
# get only body of a 200 status code response
curl -sL /dev/null GET "%{http_code}\n" "$1"
