#' ISBN-10 validity formula 
isbn10__ <- function(isbn10)  (t(isbn10) %*% 10:1) %% 11 == 0

#' ISBN-10 Verifier
#' 
#' The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a 
#' digit or an X only). In the case the check character is an X, this represents 
#' the value '10'. These may be communicated with or without hyphens, and can be 
#' checked for their validity by the following formula:
#' 
#' (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + 
#'  d₉ * 2 + d₁₀ * 1) mod 11 == 0
#' 
#' If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.
#' 
#' Exercise resource: `https://exercism.org/tracks/r/exercises/isbn-verifier`
#' 
#' Useful regex resources: `https://regex101.com/`
#' 
#' @param isbn A string.
#' 
#' @return A logical value. TRUE is the input is a valid isbn-10.
#' 
#' @details This function starts with a series of verification before compute the
#' validity formula (`isbn10__`):
#' 1. If the input number string contains 10 digits
#' 2. If the input number string starts with 9 digits (0 to 9)
#' 3. If the check character a digit or an "X"
#' If either of these three format verification fails, the function will throw 
#' an error message instead of carry out computing the validity formula.
#' 
#' @examples
#' isISBN10("3-598-21508-8")
#' isISBN10("3-598-21507-X")
#' 
#' @export
isISBN10 <- function(isbn) {

    if (is.character(isbn) == FALSE)
        stop("The input must be a string!")

    isbn <- gsub("-", "", isbn)

    if (nchar(isbn) != 10) 
        stop("An isbn-10 must contain exactly 10 digits!")

    if (grepl("^[0-9]{9}", isbn) == FALSE)
        stop("The first 9 digits of an isbn-10 must be numeric digits!")

    if (grepl("[0-9X]", substr(isbn, 10, 10)) == FALSE) 
        stop("The check character (last digit) must be a digit or X!")
   
    isbn10 <- strsplit(isbn, NULL)
    if (substr(isbn, 10, 10) == "X") isbn10[[1]][10] <- "10"

    isbn10 <- sapply(isbn10, as.numeric)
    
    return(isbn10__(isbn10)[[1]])
   
}
