#!/bin/bash
# grep the conetent length
curl -sI "$1" | grep "Content-Length:" | cut -c 17-
