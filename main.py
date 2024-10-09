from Scrapping.Indeed import main_scrape

## Indeed Example

main_scrape("data+scientist", "United+States", "1", 3).to_csv(
    "Sample1.csv", index=False
)
