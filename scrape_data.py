import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = "https://bongda24h.vn/nhan-dinh-bong-da-c344-p1.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    match_data = []
    for article in soup.select('div.section-content > article'):
        match_title = article.select_one('header > h3').text.strip() if article.select_one('header > h3') else "N/A"
        match_time = article.select_one('header > p.article-meta > span').text.strip() if article.select_one('header > p.article-meta > span') else "N/A"
        league = article.select_one('header > p.article-meta').text.strip() if article.select_one('header > p.article-meta') else "N/A"
        home_team = article.select_one('header > p.article-meta > a:nth-of-type(1)').text.strip() if article.select_one('header > p.article-meta > a:nth-of-type(1)') else "N/A"
        away_team = article.select_one('header > p.article-meta > a:nth-of-type(2)').text.strip() if article.select_one('header > p.article-meta > a:nth-of-type(2)') else "N/A"
        home_logo = article.select_one('p > a > picture > img')['src'] if article.select_one('p > a > picture > img') else "N/A"
        away_logo = article.select_one('p > a:nth-of-type(2) > picture > img')['src'] if article.select_one('p > a:nth-of-type(2) > picture > img') else "N/A"
        content = article.select_one('header > p.article-summary').text.strip() if article.select_one('header > p.article-summary') else "N/A"

        match_data.append({
            "Title": match_title,
            "MatchTime": match_time,
            "League": league,
            "HomeName": home_team,
            "AwayName": away_team,
            "HomeLogo": home_logo,
            "AwayLogo": away_logo,
            "Content": content
        })

    return match_data
