def get_pictures(keyword):
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1920,1200")
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    driver.get(f"https://pixabay.com/images/search/{keyword}/")
    response = driver.page_source
    driver.quit()

    soup = BeautifulSoup(response, 'lxml')

    for d in soup.find_all('div', {'class': 'container--3NC_b'})[:10]:
        src = d.find('a').findChildren()[0]['src']
        print(src)


get_pictures('wind')
