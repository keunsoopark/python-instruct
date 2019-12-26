// To use tail call optimization, the recursive function return the function itself.

// ex-1) tail call optimization possible
function canTailRecurse (arg) {
    //
    return canTailRecurse(arg)
}

// ex-2) tail Call optimization impossible
function canNotTailRecurse (arg) {
    let n;
    //
    return n * canNotTailRecurse(arg)
}