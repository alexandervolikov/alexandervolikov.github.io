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

  {% if item.img != 0 %}
    <a href="{{ site.baseurl }}{{ item.permalink }}"><img src="{{ item.img }}"/></a>
  {% endif %}

  {{ item.short }}
  <hr>
{% endfor %}