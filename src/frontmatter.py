def set_wrapper(wrapper) :
    '''
    Write a string and put a line break at the end.

    :param wrapper: wrapper's string.
    :type wrapper: string

    :return: wrapper's string with a line break at the end.
    :rtype: string
    '''
    line_wrapper = f"{wrapper}\n"
    return line_wrapper

def set_newlines(newlines) :
    '''
    Generate a string with the quantity of linebreaks desired.

    :param newlines: number of linebreaks.
    :type wrapper: int

    :return: string with the linebreaks desired.
    :rtype: string
    '''
    after = ""
    for i in range(newlines) :
        after = after + "\n"
    return after


def set_data(data) :
    '''
    Transform data from a dictionary type to an organized string.

    :param data: frontmatter's data
    :type data: dictionary

    :return: a sorted string where data is printed according its type.
    :rtype: string
    '''

    data_sorted = sorted(data.items(), key=lambda x: x[0]) #Ordena el diccionari alfabèticament per key i el transforma en llista de tuples.

    fm_data = ""
    for tupla in data_sorted:
        key = tupla[0]
        value = tupla[1]
        if type(value)==str :
            fm_data += f"{key}: '{value}'" + "\n"
        elif type(value)==bool:
            value = str(value)
            value = value.lower()
            fm_data += f"{key}: {value}" + "\n"
        else :
            value = str(value)
            fm_data += f"{key}: {value}" + "\n"
    return fm_data


def frontmatter(filename: str, data: dict, begin: str = "---", end: str = "---", after: int = 2) :
    '''
    Write a frontmatter at the beginning of a file.

    :param filename: file
    :type filename: file
    :param data: frontmatter's data.
    :type data: dictionary
    :param begin: the wrapper put at the beginning of the frontmatter
    :type begin: str
    :param end: the wrapper put at the end of the frontmatter
    :type end: str
    :param after: number of line breaks between frontmatter and text
    :type after: int

    :return: a file with a frontmatter
    :rtype: file
    '''
    
    if not isinstance(data, dict) :
        print("frontmatter's data type must be dictionary")
        raise SystemExit

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

    fm_data = set_data(data)
    fm_begin = set_wrapper(begin) # Cadena de caràcters de l'inici
    fm_end = set_wrapper(end) # Cadena de caràcters del final
    fm_newlines = set_newlines(after)

    # Reescrivim de nou l'arxiu
    handle.write(fm_begin)
    handle.write(fm_data)
    handle.write(fm_end)
    handle.write(fm_newlines)

    handle.write(text)

    return handle.close()