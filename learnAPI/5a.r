library(jsonlite)
library(dplyr)
library(httr)
library(tibble)
library(tidyr)

url <- "https://api.zippopotam.us/us/10006"

response <- GET(url)

if (http_status(response)$category == "Success") {
    json_content <- content(response, "text")
    data <- fromJSON(json_content)

    df <- as.data.frame(data)
    print(head(df))
    cat('\n\n\n')

    entry <- data
    data <- data$places

    df <- data.frame(
        post_code = entry$`post code`,
        country = entry$country,
        country_code = entry$`country abbreviation`,
        place = data$`place name`,
        state = data$state,
        state_abbreviation = data$`state abbreviation`,
        longitude = data$longitude,
        latitude = data$latitude
    )
    print(df)
}
