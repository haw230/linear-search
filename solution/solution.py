def solved_search(ls, num):
    for i in range(len(ls)): #for every index of ls, starting from 0, going up by one
        if ls[i] == num: #if the value of this index is what we're looking for
            return i #that is the location, function is complete
    return -1 #this would only return if "return i" has never been reached throughout the iteration of the entire list