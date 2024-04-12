library(jsonlite)
library(dplyr)
library(httr)
library(tibble)
library(tidyr)

url <- "https://official-joke-api.appspot.com/random_joke"

response <- GET(url)

if (http_status(response)$category == "Success") {
    json_content <- content(response, "text")
    data <- fromJSON(json_content)

    df <- t(as.data.frame(data))
    colnames(df) <- 'Joke'
    print(head(df))
}
