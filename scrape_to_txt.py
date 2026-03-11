import urllib.request
import re
import os

urls = [
    "", "about-us/", "our-services/", "cybersecurity/", "it-security/", 
    "endpoint-management/", "core-industry/", "trainings/", "job-openings/", 
    "industries/", "portfolio/", "our-clients/", "gallery/", "leadership-team/", 
    "blog/", "get-a-quote/", "faq/", "team-member/", "career/"
]

base_url = "https://cyberfyx.net/"
output_dir = "raw_scraped_data"
os.makedirs(output_dir, exist_ok=True)

for u in urls:
    url = base_url + u
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')
        
        # Strip out scripts and styles
        text = re.sub(r'<style.*?</style>', '', html, flags=re.DOTALL|re.IGNORECASE)
        text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL|re.IGNORECASE)
        # Strip remaining HTML tags
        text = re.sub(r'<[^>]+>', ' \n ', text)
        # Clean up excessive whitespace
        text = re.sub(r'\n\s*\n', '\n', text)
        text = re.sub(r' {2,}', ' ', text).strip()
        
        filename = u.replace('/', '_').strip('_')
        if not filename: 
            filename = 'home'
            
        filepath = os.path.join(output_dir, f"{filename}.txt")
        with open(filepath, "w", encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write("="*50 + "\n\n")
            f.write(text)
        print(f"Successfully saved {filepath}")
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
