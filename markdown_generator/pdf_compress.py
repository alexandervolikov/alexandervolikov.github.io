
#%%
def parse_publication(text):
  """
  Parses a BibTeX entry in text format and extracts title, doi, and author list.

  Args:
      text: The BibTeX entry in text format.

  Returns:
      A dictionary containing the extracted title, doi, and author list,
      or None if parsing fails.
  """
  data = {}
  for line in text.splitlines():
    if line.startswith("@"):
      data['name'] = line[9:-1]
    parts = line.strip().split(" = ", 1)
    if len(parts) == 2:
      key, value = parts
      value = value.replace("{","")
      value = value.replace(":","-")
      value = value.replace("}","")
      if key == 'author':
        value = value.replace(" and ", "; ")
      data[key.lower()] = value[:-1]
  return data
#%%

publications = {}
with open("papers.bib", "r") as file:
  text = ""
  for line in file:
    if line.startswith("@"):
      if text:
        publication = parse_publication(text)
        if publication:
          publications[publication["title"]] = publication
      text = line
    else:
      text += line
  publication = parse_publication(text)
  if publication:
    publications[publication["title"]] = publication

print(publications)

if publications:
  for title, publication in publications.items():
    print(f"\nTitle: {publication['title']}")
    print(f"DOI: {publication['doi']}")
    print(f"year: {publication['year']}")
    print(f"Authors: {publication['author']}")
    if 'abstract' in publication:
      print(f"Abstract: {publication['abstract']}")
else:
  print("No publications found in the BibTeX file.")
# %%
for title, publication in publications.items():
  if 'abstract' not in publication:
      publication['abstract'] = ""
  filename = f"{publication['year']}_{publication['journal']}_{publication['title'][:5]}.md"
  fg = f"permalink: /publication/{publication['year']}_{publication['journal']}_{publication['title'][:5]}"
  with open(filename, "w") as f:
    f.write(f"---\n{fg}\ncollection: publications\ntitle: {publication['title']}\nauthor: {publication['author']}\nyear: {publication['year']}\ndoi: {publication['doi']}\n\n---\n\n{publication['abstract']}\n")
# %%
