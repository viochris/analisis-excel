library(jsonlite)
library(dplyr)
library(httr)
library(tibble)
library(tidyr)

url <- "https://api.coindesk.com/v1/bpi/currentprice.json"

response <- GET(url)

if (http_status(response)$category == "Success") {
    json_content <- content(response, "text")
    data <- fromJSON(json_content)

    df <- t(as.data.frame(data$bpi$USD))
    print(df)



    df <- as.data.frame(data$time)
    print(df)
} else {
    cat("Permintaan tidak berhasil. Kode status:", http_status(response)$status_code)
}

