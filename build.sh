#!/bin/bash

hugo --theme=hugo-zen
cd public
git add --all
git commit -m "Automatic page build"
git push origin master
cd ..
