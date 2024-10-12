from src.scrapers import VibeScraper, YoutubeScraper

vibe_scraper = VibeScraper()
target_info_by_vibe = vibe_scraper.get_target_info_by_vibe()
target_info_by_vibe['searchKeyword'] = target_info_by_vibe.apply(lambda x: f"{x['artistName']} {x['trackTitle']} official MV", axis=1)

youtube_scraper = YoutubeScraper()
youtube_scraper.update_channel_info_sheet()

meta_by_youtube = youtube_scraper.crawl_youtube_search(target_info_by_vibe['searchKeyword'].unique())
meta_by_3rd_party = youtube_scraper.crawl_content_info_by_3rd_party(meta_by_youtube['mv_identifier'].unique())
total_youtube_info = meta_by_youtube.merge(meta_by_3rd_party, on='mv_identifier', how='left')

total_info = target_info_by_vibe.merge(
    total_youtube_info,
    on='searchKeyword',
    how='left',
)
