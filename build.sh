#!/bin/bash

hugo --theme=hugo-icarus-theme
cd public
git add --all
git commit -m "Automatic page build"
git push origin master
cd ..
git add .
git commit -m "Automatic repo commit"
git push origin master
