import requests
import xml.etree.ElementTree as ET

# Fetch the XML content
sitemap_url = "https://threatradar.net/wp-sitemap-posts-post-1.xml"
response = requests.get(sitemap_url)

if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content)
    
    # Iterate through each <url> tag
    for url in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        loc = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
        lastmod = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod").text
        print(" Url:", loc,"\n","Date:", lastmod)
        print("\n")
else:
    print("Failed to fetch the sitemap.")
