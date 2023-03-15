import json

from pprint import pprint

from twitter_scraper_selenium import scrape_profile, get_profile_details

# microsoft = scrape_profile(
#     twitter_username="microsoft",
#     output_format="json",
#     browser="firefox",
#     headless=False,
#     tweets_count=5,
# )

microsoft = get_profile_details(
    twitter_username="microsoft",
    output_format="json",
    browser="firefox",
    headless=False,
)


pprint(json.loads(microsoft))
