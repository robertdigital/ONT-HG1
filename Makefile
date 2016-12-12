all:
	jekyll build --future --incremental

deps:
	sudo gem install jekyll jekyll-theme-primer
