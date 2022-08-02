def frontmatter(filename: str, begin: str = "---", end: str = "---", newlines_after: int = 2, **kwargs) :
    '''
    Write a frontmatter at the beginning of a file.

    :param filename: file
    :type filename: file
    :param begin: the wrapper put at the beginning of the frontmatter
    :type begin: str
    :param end: the wrapper put at the end of the frontmatter
    :type end: str
    :param newlines_after: number of line breaks between frontmatter and text
    :type newlines_after: int

    :return: a file with a frontmatter
    :rtype: file
    '''

    try :
        handle = open(filename,"r") # Obre l'arxiu en mode lectura
    except OSError as err : # Guarda la frase del tipus d'error a err
        print("OS error: {0}".format(err)) # Mostra el tipus d'error
        raise SystemExit

    text = handle.read() # Guarda el text ja existent en l'arxiu
    handle.close()

    try :
        handle = open(filename,"w") # Obre l'arxiu en mode escriptura sobreescrita 
    except OSError as err :
        print("OS error: {0}".format(err))
        raise SystemExit        


    kwargs_sorted = sorted(kwargs.items(), key=lambda x: x[0]) #Ordena el diccionari alfabèticament per key i el transforma en llista de tuples.
    data = ""
    for tupla in kwargs_sorted:
        key = tupla[0]
        value = tupla[1]
        if type(value)==str :
            data = data + f"{key}: '{value}'" + "\n"
        elif type(value)==bool:
            value = str(value)
            value = value.lower()
            data = data + f"{key}: {value}" + "\n"
        else :
            value = str(value)
            data = data + f"{key}: {value}" + "\n"

    begin_wrapper = f"{begin}\n" # Cadena de caràcters de l'inici
    end_wrapper = f"{end}\n" # Cadena de caràcters del final
  
    after = "" # Genera cadena amb els salts de línea indicats
    for i in range(newlines_after) :
        after = after + "\n"

    handle.write(begin_wrapper) # Reescrivim de nou l'arxiu
    handle.write(data)
    handle.write(end_wrapper)
    handle.write(after)

    handle.write(text)

    return handle.close()



filename = "file.md"
data = {"videos" : ["iymN_CPNVwQ", "nHi3YWQAyB4"], "description": "Lorem ipsum", "difficulty" : 3, "fieldNumber" : 1, "hasExercises" : True, "hasRelated" : True, "hasVideos" : True, "language" : "es", "layout" : "layouts/topic.html", "name" : "Suma de matrices", "parentName" : "Operaciones con matrices", "permalink" : "/{{language}}/{{section}}/{{name | slug}}/", "readingTime" : 10, "related" : ["Producto de matrices", "Matriz transpuesta"], "section" : "temas", "sectionExercises" : "ejercicios", "syllabusSection" : "temario", "title" : "Suma de matrices"}

frontmatter(filename, **data)