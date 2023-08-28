
def multiToOne(multiCon, pathStr):
    oneDimDict = {}
    multiConType = type(multiCon)
    
    if(multiConType == dict or multiConType == list or multiConType == tuple):
        for i, key in enumerate(multiCon):
            pathExtension = ''
            # if dictionary use key values, else if list/tuple use index values
            if(pathStr == ''):
                pathExtension += str(key) if (multiConType == dict) else str(i)
            else:
                pathExtension += f'/{key}' if (multiConType == dict) else f'/{str(i)}'
            
            pathDict = multiToOne(multiCon[key], pathStr+pathExtension) if (multiConType == dict) else multiToOne(multiCon[i], pathStr+pathExtension)
            for k in pathDict:
                oneDimDict[k] = pathDict[k]
    # otherwise it's some value
    else:
        oneDimDict[pathStr] = multiCon

    return oneDimDict

# Assuming for now that we aren't considering tuples as
# a possible container, since the indices are the same as lists
# Also assuming dictionaries won't contain '0' or other numeric values
# as keys, and reserving those for lists

def oneToMulti(oneArr):
    return