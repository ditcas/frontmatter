
filename = "file.md"

frontmatter_data = {"videos" : ["iymN_CPNVwQ", "nHi3YWQAyB4"], "description": "Lorem ipsum", "difficulty" : 3, "fieldNumber" : 1, "hasExercises" : True, "hasRelated" : True, "hasVideos" : True, "language" : "es", "layout" : "layouts/topic.html", "name" : "Suma de matrices", "parentName" : "Operaciones con matrices", "permalink" : "/{{language}}/{{section}}/{{name | slug}}/", "readingTime" : 10, "related" : ["Producto de matrices", "Matriz transpuesta"], "section" : "temas", "sectionExercises" : "ejercicios", "syllabusSection" : "temario", "title" : "Suma de matrices"}

import frontmatter as fm
from frontmatter import frontmatter

fm.frontmatter(filename, frontmatter_data)