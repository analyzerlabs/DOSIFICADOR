#!/bin/bash
git config --global user.email "fisicomiguel@gmail.com"
git config --global user.name "analyzerlabs"
git pull
git add .
git commit -m "$*"
git pu