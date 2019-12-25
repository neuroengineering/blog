# MSNE Student Blog


Blog posts are written using Markdown.
Refer to the exapmles in `content/post/*.md` for references.

The general workflow might look like this:

- `git pull origin master` for grabbing the latest changes
- `git submodule update --recursive --remote` for grabbing the latest version of the submodules
- Editing articles and updating content as you like.
    - Blog posts go to `content/post/*.md`
    - Images go to `static/img/`. Use a separate folder if the post requires many images. Use single images directly if you only need a header. Please add the date of the events to the image prefix.
- Test your changes using ``make serve`` and check the page on [http://localhost:1313/](http://localhost:1313/).
- After finishing, build the page and commit your changes by running `make all` in the root directory.


## Contact

Maintained by [Steffen Schneider](http://stes.io). Open an issue here or contact me in case of any questions.
