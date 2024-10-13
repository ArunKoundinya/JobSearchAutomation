from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    driver = webdriver.Chrome(options=options)
    return driver


def extractlists(inputlist, index):
    oextractlists = []
    for i in range(0, index):
        oextractlists.append(inputlist[i].get_attribute("innerText"))
    return oextractlists


def extracthref(inputlist, index):
    oextracthref = []
    for i in range(0, index):
        oextracthref.append(inputlist[i].get_attribute("href"))
    return oextracthref


def scrape_indeed(search, location, age, pages):
    JobTitles = []
    CompanyName = []
    JobLocation = []
    JobLink = []
    Salary = []
    JobType = []
    Skills = []
    keyskillslist = [
        "python",
        "sql",
        "r",
        "sql",
        "ml-ops",
        "cloud",
        "nlp",
        "deep learning",
        "simulation",
        "optimization",
        "presentation",
        "communication",
        "actionable",
        "ai/ml",
        "predictive",
        "tensorflow",
        "hadoop",
        "regresion",
        "sci-kit",
        "clustering",
        "visualization",
        "problem-solving",
        "articulate",
        "natural",
        "consumer-facing",
        "consumer-centric",
        "nosql",
        "aws",
        "leadership",
        "KPIs",
        "KPI",
        "lead",
        "PHD",
        "Masters",
        "experience",
        "strategy",
        "forecasting",
        "uncover",
        "dashboards",
        "reports",
        "analytics",
        "alliance",
        "influence",
        "individual",
    ]

    baseurl = (
        "https://www.indeed.com/jobs?q=" + search + "&l=" + location + "&fromage=" + age
    )
    driver = web_driver()
    driver.maximize_window()
    wait = WebDriverWait(driver, 40)

    for page in range(0, pages):
        try:
            url1 = baseurl if page == 0 else baseurl + "&start=" + str(page * 10)
            driver.get(url1)
            wait.until(
                lambda e: e.execute_script("return document.readyState") != "loading"
            )
            jobtitles = driver.find_elements(
                By.CSS_SELECTOR, "h2.jobTitle.css-198pbd.eu4oa1w0"
            )
            urls = driver.find_elements(
                By.CSS_SELECTOR, "a.jcs-JobTitle.css-jspxzf.eu4oa1w0"
            )
            companyname = driver.find_elements(
                By.CSS_SELECTOR, "span.css-63koeb.eu4oa1w0"
            )
            joblocation = driver.find_elements(
                By.CSS_SELECTOR, "div.css-1p0sjhy.eu4oa1w0"
            )

            JobTitles.extend(extractlists(jobtitles, len(jobtitles)))
            JobLink.extend(extracthref(urls, len(urls)))
            CompanyName.extend(extractlists(companyname, len(companyname)))
            JobLocation.extend(extractlists(joblocation, len(joblocation)))

        except:
            break

    for i in range(0, len(JobLink)):
        driver.get(JobLink[i])
        wait.until(
            lambda e: e.execute_script("return document.readyState") != "loading"
        )
        try:
            salary_jobtype = driver.find_elements(
                By.CSS_SELECTOR, "div.js-match-insights-provider-1m98ica.e1xnxm2i0"
            )
            Salary.append(salary_jobtype[0].text)
        except:
            Salary.append(str("InfoNotAvailable"))

        try:
            JobType.append(salary_jobtype[1].text)
            del salary_jobtype
        except:
            JobType.append(str("InfoNotAvailable"))
            del salary_jobtype

        try:
            description = driver.find_element(
                By.CSS_SELECTOR,
                "div#jobDescriptionText.jobsearch-JobComponent-description.css-16y4thd.eu4oa1w0",
            )
            Skills.append(
                list(
                    set(description.text.lower().split(" ")).intersection(keyskillslist)
                )
            )
        except:
            Skills.append(str("InfoNotAvailable"))
            description = ""
            del description

    Dict = {
        "JobTitles": JobTitles,
        "CompanyName": CompanyName,
        "JobLocation": JobLocation,
        "JobLink": JobLink,
        "Salary": Salary,
        "JobType": JobType,
        "Skills": Skills,
    }

    driver.quit()

    return pd.DataFrame(Dict)
