# Job Search Automation
Purpose:
This repository is designed to help recent graduates and undergraduates automate job searches, saving valuable time and effort. It is actively maintained, with regular updates to include new variables and additional job sites.

Contributions and feedback are welcome! Please feel free to fork or clone this repository, and raise any issues or suggestions directly on GitHub.

## Getting Started with GitHub Codespaces

Follow these steps to set up and run the project in your GitHub Codespace environment.

### Step 1: Create a Virtual Environment

```bash
virtualenv ~/.venv
source ~/.venv/bin/activate
```

### Step 2: Install Python Dependencies
Install all required Python packages:
```bash
make install
```

### Step 3: Install System Dependencies
Update your package list and install system requirements:
```bash
sudo apt-get update
sudo apt-get install chromium-browser
sudo apt-get install chromium-chromedriver
```

### Step 4: Verify Code Functionality
Run the following command to check code correctness:
```bash
make all
```

### Step 5: Run the Main Script
Run the script to start scraping job data:
```bash
python main.py
```
After running the script, a .csv file containing the job data will be generated.

## Customizing the Job Search

To customize the job search parameters, modify the following function call:
```python
main_scrape("data+scientist", "United+States", "1", 3).to_csv(
    "Sample1.csv", index=False
)
```
- First Parameter: Job title or keyword (e.g., "data+scientist")
- Second Parameter: Location (e.g., "United+States")
- Third Parameter: Job age (set this to "1" for best results)
- Fourth Parameter: Number of pages to scrape (e.g., 3)
