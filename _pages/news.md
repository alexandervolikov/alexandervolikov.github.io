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


  ![{{ item.title }}]("https://github.com/alexandervolikov/alexandervolikov.github.io/tree/main/{{ item.img }}")
  
  {{ item.short }}
  <hr>
{% endfor %}