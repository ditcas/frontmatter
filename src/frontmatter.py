def frontmatter(filename) :

    try :
        handle = open(filename,"r")
    except OSError as err : # Guardem la frase del tipus d'error a err
        print("OS error: {0}".format(err)) #Mostrem el tipus d'error
        raise SystemExit

    text = handle.read()

    try :
        handle = open(filename,"w")
    except OSError as err :
        print("OS error: {0}".format(err))
        raise SystemExit        

    first = "---\n"
    line1 = "Text afegit a posteriori\n"
    end = "---\n\n"

    handle.write(first)
    handle.write(line1)
    handle.write(end)

    handle.write(text)

    return handle.close()

frontmatter("file.md")