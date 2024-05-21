---
permalink: /
title: "Alexander Volikov, PhD"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div class="container">
    <img src="{{ site.baseurl }}/images/about1.jpg"/>
</div>

## About Me

Hello! I'm Alexander, an environmental chemist and project leader at the Max Planck Institute of Colloids and Interfaces.  My research group focuses on humic matter systems, exploring ways to convert biomass into artificial humic substances. We delve into both the synthesis and potential applications of these materials.  Personally, I'm fascinated by how environmental factors influence the evolution of organic matter. Learn more about our research on [humic matter systems](https://alexandervolikov.github.io/research/)

Feel free to reach out to me for research discussions or potential collaborations.

## Last News

{% assign sorted = site.posts | sort: 'date' | reverse %}
{% for item in sorted limit:1 %}
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

## [Read more news](https://alexandervolikov.github.io/news/)

{% assign all_tags = '' | split: ',' %}

 {% for post in site.posts %}
    {% for tags in post.tags %}
        {% for tag in tags %}
            {% assign all_tags = all_tags | push: tag %}
        {% endfor %}
    {% endfor %}
{% endfor %}

{% assign all_tags = all_tags | sort %}
{% assign all_tags = all_tags | uniq %}

<ul class="tag-list">
    {% for tag in all_tags %}
        <li><a href="{{ site.tag_dir | prepend: '/' }}/{{ tag | uri_escape }}">{{ tag }}</a></li>
    {% endfor %}

</ul>


<div class="container">
    <img src="{{ site.baseurl }}/images/about2.jpg"/>
</div>