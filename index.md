---
layout: default
title: Home
published: true
---
<h1>{{ page.title }}</h1>
<ul>
  {% for post in site.posts %}
  <li>
  <a href="{{ post.url }}">{{ post.title }}</a>
  {{ post.excerpt }}
  </li>
  {% endfor %}
</ul>

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi cursus est vel molestie ullamcorper. Fusce ac ligula dignissim, tristique turpis a, vulputate magna. Mauris pulvinar velit sit amet risus finibus, molestie malesuada tellus ullamcorper. Fusce dictum posuere sem. Aliquam lacinia ex non sem aliquet ornare. Fusce eu sapien augue. Vivamus nisi lectus, tristique ultricies tristique ac, vehicula nec diam. In tincidunt orci non gravida varius. In non risus nec sem lobortis fringilla. Praesent at gravida odio, quis vehicula orci. Vivamus tempus enim eget molestie fermentum. Proin convallis nunc ut nunc dictum, at tempor massa fermentum. Donec eu leo consectetur, mollis purus sit amet, accumsan magna.

Curabitur laoreet pulvinar dolor, ut mollis erat luctus a. Pellentesque viverra lacus a accumsan laoreet. Nunc venenatis dictum odio, ut bibendum ipsum porttitor sed. Nullam quis libero malesuada, efficitur dolor non, luctus orci. Integer vel semper nibh. Nunc et accumsan neque. Pellentesque vel mi odio. Donec iaculis interdum turpis, sed pulvinar lacus lobortis a. Proin at porttitor quam, quis tristique nisi.

Nam felis urna, gravida nec sagittis eget, iaculis sit amet ante. Phasellus dictum ut elit vitae iaculis. Ut tincidunt purus quis lorem ornare elementum. Sed vitae vestibulum lectus, in feugiat enim. Maecenas vulputate at nibh eget rhoncus. Aenean dapibus ut dolor eget sollicitudin. Donec vestibulum augue id orci eleifend ullamcorper. Donec ultricies blandit volutpat. Nullam porttitor turpis finibus, malesuada augue ac, pharetra mauris. Proin at arcu ante. Ut rhoncus eros sed mauris convallis tincidunt. Curabitur vel ex enim. Suspendisse potenti. Phasellus vulputate ac leo vitae tristique. Nullam eget ipsum eros. Mauris vehicula eros non placerat posuere.
<style>
div.gallery {
    display: -ms-flexbox;
    -ms-flex-wrap: wrap;
    -ms-flex-direction: column;
    -webkit-flex-flow: row wrap;
    flex-flow: row wrap;
    display: -webkit-box;
    display: flex;
}
div.img {
    margin: 5px;
    border: 1px solid #ccc;
    left;
    width: 180px;
    display: inline-block;
    -webkit-box-flex: auto;
    -ms-flex: auto;
    flex: auto;
    width: 200px;
    margin: .5vw;
}

div.img:hover {
    border: 1px solid #777;
}

div.img img {
    width: 100%;
    height: auto;
}

div.desc {
    padding: 15px;
    text-align: center;
}
</style>
<div class="gallery">
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0567.jpg">
      <img src="/images/800x600/IMG_0567.jpg" alt="blood letting" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0573.jpg">
      <img src="/images/800x600/IMG_0573.jpg" alt="samples extracted" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0584.jpg">
      <img src="/images/800x600/IMG_0584.jpg" alt="plasma" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0586.jpg">
      <img src="/images/800x600/IMG_0586.jpg" alt="biohazard" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0588.jpg">
      <img src="/images/800x600/IMG_0588.jpg" alt="setup" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0591.jpg">
      <img src="/images/800x600/IMG_0591.jpg" alt="parallel processing" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0593.jpg">
      <img src="/images/800x600/IMG_0593.jpg" alt="flowcells" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0594.jpg">
      <img src="/images/800x600/IMG_0594.jpg" alt="preparation" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0596.jpg">
      <img src="/images/800x600/IMG_0596.jpg" alt="sample loading" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0597.jpg">
      <img src="/images/800x600/IMG_0597.jpg" alt="data" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
  <div class="img">
    <a target="_blank" href="/images/800x600/IMG_0603.jpg">
      <img src="/images/800x600/IMG_0603.jpg" alt="promethion" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
</div>
