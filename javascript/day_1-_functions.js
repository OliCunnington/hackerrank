
/*
 * Create the function factorial here
 */
function factorial(n) {
    if (n == 2) {
        return 2
    } else {
        return n*factorial(n-1)
    }
}

