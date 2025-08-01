#!/bin/bash
# Bash script that takes  an argument, sends a GET request to the URL, and displays the response
curl -sH "X-School-User-Id: 98" "$1"
