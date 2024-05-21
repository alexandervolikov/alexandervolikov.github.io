---
layout: archive
permalink: /news/
title: "News"
author_profile: false
redirect_from:
  - /wordpress/post-posts/
---

{% assign sorted = site.posts | sort: 'date' | reverse %}
{% for item in sorted limit:20 %}
  [{{ item.title }}]({{ site.baseurl }}{{ item.permalink }})
  <time datetime="{{ item.date | default: "1900-01-01" | date_to_xmlschema }}">{{ item.date | default: "1900-01-01" | date: "%B %d, %Y" }}</time>

  <div class="container">
    {% if item.img != 0 %}
      <a href="{{ item.permalink }}" ><img src="{{ site.baseurl }}{{ item.img }}" style="width: 300px;"/></a>
    {% endif %}
  </div>
  
  {{ item.short }}
  <hr>
{% endfor %}

# [View All Archive]({{ site.baseurl }}/year-archive)