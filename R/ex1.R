split__ <- function(text, size = 5){
    if (size == 0) return(text)
    strsplit(text, 
             paste0("(?<=.{", size, "})"),
             perl = TRUE)[[1]]
}

#' Atbash cipher
#' 
#' The Atbash cipher is a simple substitution cipher that relies on transposing 
#' all the letters in the alphabet such that the resulting alphabet is backwards. 
#' The first letter is replaced with the last letter, the second with the 
#' second-last, and so on.
#' 
#' @param text String
#' @param size Integer. Split the output string into chunks of this size. The 
#' default is 5.
#' 
#' @return String
#' 
#' @examples
#' encrypt("test")
#' encrypt("x123 yes", 0)
#' 
#' 
#' @export
encrypt <- function(text, size = 5) {

    cipher <- c(sort(letters, decreasing=TRUE),
                0:9)

    text <- gsub("[[:punct:]]", "", tolower(text))
    text <- gsub("\\s+", "", text)

    res <- sapply(strsplit(text, NULL)[[1]], function(chr) { 
        return(cipher[which(c(letters, 0:9) == chr)])
    })

    split__(
        paste(res, collapse=""),
        size
    )

}

