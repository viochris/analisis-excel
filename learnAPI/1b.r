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
    colnames(df) <- 'USD'
    print(df)

    df <- t(as.data.frame(data$time))
    colnames(df) <-'time'
    print(df)


    for (key in names(data$time)){
        print(key)
    }
    for (key in data$time){
        print(key)
    }
} else {
    cat("Permintaan tidak berhasil. Kode status:", http_status(response)$status_code)
}

