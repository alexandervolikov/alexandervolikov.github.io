---
permalink: /
title: "Alexander Volikov, PhD"
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<img align="left" src="https://alexandervolikov.github.io/images/profile.jpg" alt="Photo" style="width: 220px; border-radius: 10px; padding: 16px 8px 8px 8px; margin-right: 40px;"/>
Project Leader 
[Max Planck Institute of Colloid and Interfaces](https://www.mpikg.mpg.de/)  

Email: alexandervolikov AT mpikg DOT mpg DOT de  
[[Google Scholar](https://scholar.google.ru/citations?user=aF5EgjIAAAAJ&hl) | [LinkedIn](https://www.linkedin.com/in/alexander-volikov/)] | [Instagram](https://www.instagram.com/ab.volikov/)

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
{% endfor %}

[Read more my news](https://alexandervolikov.github.io/news/)

<hr>

Word cloud based on the titles of my [publications](https://alexandervolikov.github.io/publications/)

<div class="container">
    <a href="https://alexandervolikov.github.io/publications/"><img src="{{ site.baseurl }}/images/about5.jpg "/></a>
</div>