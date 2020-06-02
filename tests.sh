#!/bin/bash

locust --headless -u 240 -r 3 -t 10m -H https://sls-eus-dev-azure-python-sorting.azurewebsites.net/api --csv azure2
