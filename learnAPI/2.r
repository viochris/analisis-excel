library(jsonlite)
library(dplyr)
library(httr)
library(tibble)
library(tidyr)

url <- "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

response <- GET(url)

if(http_status(response)$category == 'Success'){
    json_content <- content(response, 'text')
    data <- fromJSON(json_content)$data

    df <- as.data.frame(data)
    print(df)
}else {
    cat("Permintaan tidak berhasil. Kode status:", http_status(response)$status_code)
}