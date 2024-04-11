library(jsonlite)
library(dplyr)
library(httr)
library(tibble)
library(tidyr)

url <- "https://randomuser.me/api/"

response <- GET(url)

if (http_status(response)$category == "Success") {
    json_content <- content(response, "text")
    data <- fromJSON(json_content)

    df <- as.data.frame(data)
    print(head(df))
    cat('\n\n\n')

    data <- data$results

    df <- data.frame(
        Gender = data$gender,
        Title = data$name$title,
        `Full Name` = paste(data$name$first, data$name$last, sep = ' '),
        city = data$location$city,
        state = data$location$state,
        country = data$location$country
    )
    print(df)
}
