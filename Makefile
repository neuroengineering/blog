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
	cd public && git commit -m "Automatic page build" || echo "No changes to page, skipping main repository"
	cd public && git push -f origin master

push:
	git add .
	git commit -m "Automatic repo commit"
	git push origin master

serve: gen
	hugo serve

cname:
	echo neuroengineering.blog > public/CNAME

gen: studentlist projects
all: cname gen page publish push
