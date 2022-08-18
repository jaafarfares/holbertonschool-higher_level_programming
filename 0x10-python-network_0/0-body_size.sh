#!/bin/bash
# grep the conetent length
curl - sI "$1" | grep - i "Content-Length:"
