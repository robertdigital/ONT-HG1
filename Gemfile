source "https://rubygems.org"

# Make sure Jekyll 3.3 is running
gem "jekyll", "~> 3.3"

# The theme for the site
gem "jekyll-theme-primer", "~> 0.1"

require 'json'
require 'open-uri'
versions = JSON.parse(open('https://pages.github.com/versions.json').read)

gem 'github-pages', versions['github-pages']
