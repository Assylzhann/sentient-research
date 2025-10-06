import os
from datetime import datetime


os.makedirs("reports", exist_ok=True)


today = datetime.utcnow().strftime("%Y-%m-%d")
filename = f"reports/{today}-weekly.md"


content = f"""# 🗓 Weekly Report — {today}

**Summary:**  
This week’s highlights, updates, and progress notes.

---

### ✅ Key Points
- New features or ideas
- Research highlights
- Next week’s focus

---

_Generated automatically by GitHub Actions_
"""


with open(filename, "w") as f:
    f.write(content)

print(f"✅ Created weekly report: {filename}")
