# sfzd.com-Spider
### Scrapy spider scraping traditional Chinese calligraphy pictures from www.sfzd.com

The previous sfzd.cn spider itself works well, but the its content isn't as good as this sfzd.com. The latter got much more bigger and comprehensive database. So I write another spider to scrape pictures from it. 
But I only scrape the first result page due to storage limit. But one pages holds as many as 96 pictures, which is indeed enough to build a large calligraphy project.

There's no issue during scraping. All progress check and control are within the spider itself. 
You can interrupt the scraping by ctrl+C * 2 and recover the progress next time the spider is started.
