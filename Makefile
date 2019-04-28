studentlist:
	python3 build_studentlist.py

projects:	
	python3 build_projects.py

clean:
	rm -rf public/*

page:
	hugo --theme=hugo-icarus-theme

publish:
	
	cd public && git add --all
	cd public && git commit -m "Automatic page build"
	cd public && git push origin master

push:
	git add .
	git commit -m "Automatic repo commit"
	git push origin master

serve: gen
	hugo serve

gen: studentlist projects
all: gen page publish push
