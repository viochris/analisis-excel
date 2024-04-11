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

    df <- data.frame(
        post_code = data$`post code`,
        country = data$country,
        country_code = data$`country abbreviation`,
        place = data$places$`place name`,
        state = data$places$state,
        state_abbreviation = data$places$`state abbreviation`,
        longitude = data$places$longitude,
        latitude = data$places$latitude
    )
    print(df)
}
