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

    df <- as.data.frame(data$bpi)
    print(df)

    usd_data <- subset(df, select = c("USD.code", "USD.symbol", "USD.rate", "USD.description", "USD.rate_float"))
    gbp_data <- subset(df, select = c("GBP.code", "GBP.symbol", "GBP.rate", "GBP.description", "GBP.rate_float"))
    eur_data <- subset(df, select = c("EUR.code", "EUR.symbol", "EUR.rate", "EUR.description", "EUR.rate_float"))

    colnames(usd_data) <- c("code", "symbol", "rate", "description", "rate_float")
    colnames(gbp_data) <- c("code", "symbol", "rate", "description", "rate_float")
    colnames(eur_data) <- c("code", "symbol", "rate", "description", "rate_float")

    result <- rbind(usd_data, gbp_data, eur_data)
    rownames(result) <- result$code

    print(result)

    df <- as.data.frame(data$time)
    print(df)
} else {
    cat("Permintaan tidak berhasil. Kode status:", http_status(response)$status_code)
}
