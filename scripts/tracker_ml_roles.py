"""Print ML / data roles posted within MAX_AGE days from the SimplifyJobs new-grad tracker.

Usage: python3 scripts/tracker_ml_roles.py [max_age_days]
Output: age|company|role|location|apply_url  (one per line)
raw.githubusercontent.com is reachable even under the trusted network policy.
"""
import re
import sys
import urllib.request

URL = "https://raw.githubusercontent.com/SimplifyJobs/New-Grad-Positions/dev/README.md"
MAX_AGE = int(sys.argv[1]) if len(sys.argv) > 1 else 30

text = urllib.request.urlopen(URL, timeout=30).read().decode()
start = text.index("## 🤖 Data Science, AI & Machine Learning New Grad Roles")
end = text.find("\n## ", start + 10)
section = text[start:end if end > 0 else None]

last_company = ""
for row in re.findall(r"<tr>(.*?)</tr>", section, re.S):
    tds = re.findall(r"<td>(.*?)</td>", row, re.S)
    if len(tds) < 5:
        continue
    strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<.*?>", " ", s)).strip()
    company = strip(tds[0])
    if company == "↳":
        company = last_company
    last_company = company
    age = strip(tds[-1])
    m = re.match(r"(\d+)d", age)
    if not m or int(m.group(1)) > MAX_AGE:
        continue
    links = re.findall(r'href="([^"]+)"', tds[3])
    print("|".join([age, company, strip(tds[1]), strip(tds[2]), links[0] if links else ""]))
