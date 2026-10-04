# Daily job-search scout: run playbook

Active through 2026-10-26. Each daily run follows this file. Do not apply, email, or contact anyone.
The user reviews everything and acts themselves.

## Run procedure
1. Work on branch `claude/job-search-scout-setup-ug6x59` (pull latest first). State files live at the repo root:
   `targets.md`, `seen.csv`, `reports/YYYY-MM-DD.md`.
2. If today is after 2026-10-26, write nothing and stop.
3. **Network check first.** WebFetch `https://boards-api.greenhouse.io/v1/boards/skydio/jobs` and
   `https://jobs.lever.co/shieldai`. If both return EGRESS_BLOCKED, verification is impossible this run:
   still scan (steps 4-6), but every candidate goes under "Unverified", and the report's first line says
   "Blocked run: careers/ATS domains blocked by the environment network policy."
4. Search sources:
   - GitHub trackers (raw.githubusercontent.com is reachable even under the trusted policy; fetch with
     curl/python in Bash, not the GitHub MCP tools):
     run `python3 scripts/tracker_ml_roles.py 30` for the SimplifyJobs "Data Science, AI & Machine Learning"
     section, and curl `https://raw.githubusercontent.com/speedyapply/2026-AI-College-Jobs/main/NEW_GRAD_USA.md`.
     Filter for ML, CV, perception, robotics, autonomy roles in the allowed locations.
   - Careers pages / ATS for every `active` company in `targets.md` (`watch` companies on Mondays).
     ATS JSON endpoints are fastest when reachable:
     Greenhouse `https://boards-api.greenhouse.io/v1/boards/<slug>/jobs?content=true`,
     Lever `https://api.lever.co/v0/postings/<slug>?mode=json`,
     Ashby `https://api.ashbyhq.com/posting-api/job-board/<slug>?includeCompensation=true`.
   - WebSearch and the Indeed connector (`mcp__Indeed__search_jobs`) for early-career ML / CV / perception
     roles in: remote US, Birmingham AL, Huntsville AL, Atlanta GA.
5. Skip anything already in `seen.csv` unless its status is `unverified` (re-try verification for those;
   update the status if it now verifies or is closed).
6. Verify each new candidate at the source (company careers page or Greenhouse/Lever/Ashby/Workday).
   Record exact URL, posting date, location and remote policy, experience requirement, posted pay range
   or "not posted". Never estimate pay and present it as posted. Unconfirmable → "Unverified".
7. Append new rows to `seen.csv`, update `targets.md` (add fitting companies discovered, drop clear misfits
   with a reason), write `reports/YYYY-MM-DD.md`, commit, and push to the branch.
8. End the session with the report text as the final message.

## Candidate profile
- ~11 months full-time SWE (Blue Cross and Blue Shield of Alabama) + ~19 months ML internships
  (sole ML engineer at Lycoming Engines: sensor-based failure detection; Mitek: fraud and anomaly detection).
- BS CS and Applied Math (UAB, 3.91). MS CS, ML specialization, Georgia Tech, in progress (Dec 2027).
- Projects: AETHELGARD (dual-energy X-ray threat detection, physics model constraining a CNN, PyTorch);
  prediction-market trading system (statistical estimator, AWS pipeline archiving 113M order-book snapshots,
  multi-agent Claude Code workflow).
- Skills: Python, PyTorch, scikit-learn, Pandas, SQL, R, AWS, Linux, Git, computer vision. Not C++.
- U.S. citizen, no clearance. GitHub: github.com/MJMoran01

## Baseline offer to beat
AutoStore, Software AI Engineer, Atlanta, in-person, base ~$80K-$97K, no bonus/equity, robotics and
warehouse-automation ML. A role counts only if it beats this on at least one major dimension (pay,
location, interest) without being clearly worse on another.

## Lane
Production ML on perception and sensor data for physical systems: computer vision, sensor/time-series ML,
anomaly detection, robotics perception, autonomy, ML infra for those. Also OK: substantive LLM work
(fine-tuning, evaluation, inference systems), not API-wrapper "applied AI".

## Location pay floors (base)
- Remote (US): >= $85K
- Birmingham, AL area (hybrid/onsite): >= $90K
- Atlanta, GA (onsite/hybrid): >= $105K
- Huntsville, AL: >= $100K
Other locations: out of scope.

## Hard exclusions (skip without listing)
- Requires active/current clearance ("eligible"/"able to obtain" is fine).
- 4+ years as a hard minimum, or senior/staff/principal/lead titles.
- Forward-deployed, field, quant trading/research, sales engineering.
- Core work is wiring LLM APIs or no-code tools.
- Posted > 30 days ago, or not confirmable on the company's own careers page/ATS (those go to Unverified).
- Staffing-agency reposts.

## Scoring (0-10 each, show scores)
- Fit: match to lane and background.
- Level: realistic odds given requirements.
- Location: remote > Birmingham > Huntsville > Atlanta.
- Pay: posted range vs floor (0 if below floor, 5 if not posted).
- Speed: startups/small companies with direct hiring managers score higher (decision needed before Oct 26).
Overall = Fit x 2 + Level + Location + Pay + Speed.

## Report format (short; don't pad)
1. New roles ranked by Overall: company, title, location + remote policy, posted pay or "not posted",
   experience requirement, scores, two lines on fit, red flags, link.
2. Top 1-2 picks: likely hiring manager/team lead (public sources only, marked "unconfirmed"); outreach
   draft under 120 words, no em-dashes, no "fellow alum" openers; one weekend prototype idea tied to their product.
3. Unverified postings, one line each.
4. Count reviewed and skipped, with main reasons.
If nothing new clears the bar, say so in one line.
