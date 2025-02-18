#!/bin/bash

# build image
docker build . -t python3

# run container
docker run python3
