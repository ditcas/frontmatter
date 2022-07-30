def frontmatter(filename: str, begin: str = "+++", end: str = "---", newlines_after: int = 2) :

    try :
        handle = open(filename,"r") # Obre l'arxiu en mode lectura
    except OSError as err : # Guarda la frase del tipus d'error a err
        print("OS error: {0}".format(err)) # Mostra el tipus d'error
        raise SystemExit

    text = handle.read() # Guarda el text ja existent en l'arxiu

    try :
        handle = open(filename,"w") # Obre l'arxiu en mode escriptura sobreescrita 
    except OSError as err :
        print("OS error: {0}".format(err))
        raise SystemExit        

    begin_wrapper = f"{begin}\n" # Cadena de caràcters de l'inici
    line1 = "Text afegit a posteriori\n" #Capçalera
    end_wrapper = f"{end}\n" # Cadena de caràcters del final
  
    after = "" # Genera cadena amb els salts de línea indicats
    for i in range(newlines_after) :
        after = after + "\n"

    handle.write(begin_wrapper) # Reescrivim de nou l'arxiu
    handle.write(line1)
    handle.write(end_wrapper)
    handle.write(after)

    handle.write(text)

    return handle.close()

frontmatter("file.md")