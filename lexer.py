def lexem_analysis(prog):
    f = open(prog, 'r')
    strings = f.read().split('\n')
    lexems = list()
    for i in range( len(strings) ):
        lexems.append( strings[i].split(' ') )

    return lexems