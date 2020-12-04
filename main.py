import capturer.crawler as c
import export as e

queries = ["coronavirus"] # You can use this as a list
folders = ["coronavirus_captures/"] # Use folders for each query above
max_results = 15 ## Nº of results in search

for q, f in zip(queries, folders):
    def explore_search(q, f, max_results):
            videos = c.explore_videos(q, max_results)
            e.export_data(videos, f, q)

    explore_search(q, f, max_results)
