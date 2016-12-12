all:
	bundle exec jekyll build --future --incremental

deps:
# if nokogiri fails on Sierra, either:
#xcode-select --install
# or 
#bundle config build.nokogiri --use-system-libraries=true --with-xml2-include=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/usr/include/libxml2
	sudo gem install jekyll bundler
	bundle install
