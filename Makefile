studentlist:
	python3 build_studentlist.py

clean:
	rm -rf public/*

page:
	hugo --theme=hugo-icarus-theme

publish:
	
	cd public && git add --all
	cd public && git commit -m "Automatic page build"
	cd public && git push origin master
	cd public && git push msne master

push:
	git add .
	git commit -m "Automatic repo commit"
	git push origin master

all: clean page publish push
