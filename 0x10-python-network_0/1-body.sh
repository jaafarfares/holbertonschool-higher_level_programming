#!/bin/bash
# get only body of a 200 status code response
curl -s -X GET "$1" -L 200
