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

    df <- data.frame(
        Gender = data$results$gender,
        Title = data$results$name$title,
        `Full Name` = paste(data$results$name$first, data$results$name$last, sep = ' '),
        city = data$results$location$city,
        state = data$results$location$state,
        country = data$results$location$country
    )
    print(df)
}
