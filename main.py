from Scrapping.Indeed import main_scrape

## Indeed Example

main_scrape("data+science+manager", "United+States", "1", 5).to_csv(
    "datasciencemanger_8thOct.csv", index=False
)
