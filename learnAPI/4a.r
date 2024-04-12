library(jsonlite)
library(dplyr)
library(httr)
library(tibble)
library(tidyr)

data_kota <- data.frame(
    Kota = c('Indonesia', 'Japan', 'China', 'Singapore', 'Malaysia')
)

for (negara in data_kota$Kota){
    url <- sprintf("http://universities.hipolabs.com/search?country=%s", negara)
    # url <- paste("http://universities.hipolabs.com/search?country=", negara, sep = '')
    # url <- "http://universities.hipolabs.com/search?name=binus&country=Indonesia"

    response <- GET(url)

    if (http_status(response)$category == "Success") {
        json_content <- content(response, "text")
        data <- fromJSON(json_content)

        df <- as.data.frame(data)
        print(head(df))
    }
}