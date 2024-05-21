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
  <p class="page__date"><strong><i class="fa fa-fw fa-calendar" aria-hidden="true"></i> {{ site.data.ui-text[site.locale].date_label | default: "Published:" }}</strong> <time datetime="{{ item.date | default: "1900-01-01" | date_to_xmlschema }}">{{ item.date | default: "1900-01-01" | date: "%B %d, %Y" }}</time></p>

  <div class="container">
    {% if item.img != 0 %}
      <a href="{{ item.permalink }}" ><img src="{{ site.baseurl }}{{ item.img }}" style="width: 300px;"/></a>
    {% endif %}
  </div>
  
  {{ item.short }}
  <hr>
{% endfor %}