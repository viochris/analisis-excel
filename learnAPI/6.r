library(jsonlite)
library(dplyr)
library(httr)
library(tibble)
library(tidyr)

url <- "https://ipinfo.io/161.185.160.93/geo"

response <- GET(url)

if (http_status(response)$category == "Success") {
    json_content <- content(response, "text")
    data <- fromJSON(json_content)

    df <- as.data.frame(data)
    print(head(df))
}
