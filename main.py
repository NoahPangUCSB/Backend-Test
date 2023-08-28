
def multiToOne(multiCon, pathStr):
    if(type(multiCon) == dict):
        for key in multiCon:
            pathExtension = ''
            if(pathStr == ''):
                pathExtension += str(key)
            else:
                pathExtension += f'/{key}'
            

    return type(x)

# Assuming for now that we aren't considering tuples as
# a possible container, since the indices are the same as lists
# Also assuming dictionaries won't contain '0' or other numeric values
# as keys, and reserving those for lists

def oneToMulti(oneArr):
    return