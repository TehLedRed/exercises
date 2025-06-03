isArmstrong__ <- function(x) {

    digits <- as.numeric(unlist(strsplit(as.character(x), "")))
    
    k <- floor(log(x, 10) + 1)
    
    return(sum(digits**k) == x)   

}

#' Armstrong Numbers 
#' 
#' An Armstrong number is a number that is the sum of its own digits each 
#' raised to the power of the number of digits.
#' 
#' For example:
#' 9 is an Armstrong number, because 9 = 9^1 = 9
#' 10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
#' 153 is an Armstrong number, because: 
#'     153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#' 154 is not an Armstrong number, because: 
#'     154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
#' Write some code to determine whether a number is an Armstrong number.
#' 
#' source: `https://en.wikipedia.org/wiki/Narcissistic_number`
#' 
#' @param x Integer. An integer vector.
#' 
#' @return A boolean vector with element equals TRUE if it is a valid armstrong
#' number, FALSE otherwise.
#' 
#' @examples
#' isArmstrongNumber(9L)
#' isArmstrongNumber(c(9L, 10L)) 
#' 
#' @export
isArmstrongNumber <- function(x) {

    if (all(is.integer(x) & x >= 0) == FALSE)
        stop("Input must be natural number (non-negative integers)!") 
        
    return(
        sapply(x, isArmstrong__)
    )   

}

