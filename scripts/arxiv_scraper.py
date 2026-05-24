import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import datetime
import os
import time

def fetch_arxiv_papers():
    # Search for papers containing "adversarial" AND ("machine learning" OR "deep learning" OR "neural network")
    query = 'all:"adversarial" AND (all:"machine learning" OR all:"deep learning" OR all:"neural network")'
    url = f'http://export.arxiv.org/api/query?search_query={urllib.parse.quote(query)}&sortBy=submittedDate&sortOrder=descending&max_results=10'
    
    # ArXiv API requires respectful usage. We add a custom User-Agent and a 3-second delay to comply with their ethical guidelines.
    time.sleep(3) 
    
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Adversarial-Defense-Methods-Bot/1.0 (https://github.com/DevChiniwala/adversarial-defense-methods)'
        }
    )
    
    try:
        response = urllib.request.urlopen(req)
        data = response.read()
        root = ET.fromstring(data)
        
        namespace = {'atom': 'http://www.w3.org/2005/Atom'}
        
        papers = []
        for entry in root.findall('atom:entry', namespace):
            title = entry.find('atom:title', namespace).text.replace('\n', ' ').strip()
            summary = entry.find('atom:summary', namespace).text.replace('\n', ' ').strip()
            link = entry.find('atom:id', namespace).text
            published = entry.find('atom:published', namespace).text
            
            authors = [author.find('atom:name', namespace).text for author in entry.findall('atom:author', namespace)]
            author_str = " and ".join(authors)
            
            bibtex_id = f"{authors[0].split()[-1].lower()}{published[:4]}{title.split()[0].lower()}"
            
            papers.append({
                'title': title,
                'authors': author_str,
                'summary': summary,
                'link': link,
                'year': published[:4],
                'bibtex_id': bibtex_id
            })
            
        return papers
    except Exception as e:
        print(f"Error fetching from arXiv: {e}")
        return []

def format_paper(paper):
    markdown = f"### {paper['title']}\n\n"
    markdown += f"```bibtex\n@article{{{paper['bibtex_id']},\n  title={{{paper['title']}}},\n  author={{{paper['authors']}}},\n  journal={{arXiv preprint}},\n  year={{{paper['year']}}}\n}}\n```\n\n"
    
    markdown += "## Motivation\n"
    markdown += "* Review this recent paper to determine the research gap it addresses.\n"
    
    markdown += "\n## Contribution\n"
    markdown += "* Analyze the abstract to determine the novel methodology or results.\n"
    
    markdown += f"\n## Summary\n{paper['summary']}\n"
    
    markdown += f"\n## Links\n* [arXiv]({paper['link']})\n\n---\n\n"
    return markdown

def main():
    print("Initiating compliant arXiv API request...")
    papers = fetch_arxiv_papers()
    if not papers:
        print("No papers found or error occurred.")
        return
        
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    out_dir = "monthly_updates"
    os.makedirs(out_dir, exist_ok=True)
    
    filename = os.path.join(out_dir, f"papers_to_review_{current_date}.md")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Monthly arXiv Paper Suggestions ({current_date})\n\n")
        f.write("> **Data Attribution:** This data is sourced from the official [arXiv API](https://arxiv.org/help/api). We acknowledge and thank arXiv for providing open-access metadata to the research community.\n\n")
        f.write("> **Note to Maintainer:** Here are the latest pre-prints related to Adversarial ML. Review these, fill out the Motivation and Contribution bullet points, and move them to their respective year directories if they meet the repository's quality threshold.\n\n")
        
        for paper in papers:
            f.write(format_paper(paper))
            
    print(f"Generated review file: {filename}")

if __name__ == "__main__":
    main()
