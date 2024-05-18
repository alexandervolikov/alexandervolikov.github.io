---
layout: archive
permalink: /news/
title: "News"
author_profile: false
redirect_from:
  - /wordpress/post-posts/
---

{% assign sorted = site.posts | sort: 'date' | reverse %}
{% for item in sorted limit:30 %}
  [{{ item.title }}]({{ site.baseurl }}{{ item.permalink }})
  
  <div class="container">
    {% if item.img != 0 %}
      <a href="{{ item.permalink }}/" ><img src="{{ site.baseurl }}{{ item.img }}" weight=300/></a>
    {% endif %}
  </div>
  
  {{ item.short }}
  <hr>
{% endfor %}