# Cyberfyx Draft Website Content Report

## Document Purpose
This draft report is designed for leadership and marketing teams to present a practical content plan for Cyberfyx's website. It identifies:
- What content should be kept or added (relevant content),
- What content should be removed or rewritten (irrelevant content), and
- How to structure pages versus subdomains for SEO, trust, and conversions.

---

## Research Snapshot (What this draft is based on)

### What we reviewed
- Existing page captures from the current site under `raw_scraped_data/`.
- Current strengths on service pages (cybersecurity, IT security, endpoint management, training).
- Current weaknesses (template leftovers, dummy logistics content, broken/staging links).

### Key findings that shape this plan
1. Core service intent is strong, but page consistency and buyer-flow clarity are weak.
2. Several non-core pages still contain irrelevant template content (e.g., logistics placeholders), reducing trust.
3. Industries and blog areas require immediate content quality upgrades to support authority.
4. Domain structure should prioritize a single main domain path model first, with selective subdomains only where operationally necessary.

---

## Recommended Information Architecture

### Main navigation pages
- Home
- About Us
- Our Services
- Industries
- Careers
- Contact Us

### Recommended supporting sections
- Leadership Team (can remain under About)
- Case Studies
- Insights / Blog
- Compliance Resources / Downloads
- Client Success / Testimonials

---

## 1) Home

### Page goal
Establish trust quickly, explain Cyberfyx's value proposition in plain business language, and drive visitors to consultation.

### Relevant content to include
- **Clear hero statement**: who Cyberfyx helps and what outcomes it delivers.
- **Primary CTA** above the fold: "Book a Security Consultation".
- **Secondary CTA**: "Get a Quote" or "Talk to an Expert".
- **Service snapshot grid** (Cybersecurity, IT Security, Endpoint Management, Training, Core Industry support).
- **Trust proof**: certifications, leadership credentials, years of combined expertise.
- **Industry strip**: sectors served with links to industry pages.
- **Outcome-led stats**: e.g., assessments completed, avg. remediation time, audits supported.
- **Recent insights**: latest 3 posts/resources for thought leadership.

### Irrelevant content to remove
- Long, generic intros with no actionable business outcome.
- Repeated marketing lines that also appear verbatim on multiple pages.
- Any legacy logistics-theme copy/images.
- Dead or duplicate CTA buttons.

### Subdomain recommendation
- Keep Home at the root: `https://www.cyberfyx.net/`
- Avoid moving Home to any subdomain.

---

## 2) About Us

### Page goal
Build credibility with story + team + governance posture.

### Relevant content to include
- **Company narrative**: why Cyberfyx exists and what problem it solves.
- **Mission, vision, values** linked to real operating principles.
- **Leadership highlights** with domain credentials and years of experience.
- **Operating model**: consulting + implementation + managed support.
- **Governance clarity**: if KRISH CORP relation exists, explain it clearly in one section.
- **Milestone timeline**: founding, key partnerships, major delivery milestones.

### Irrelevant content to remove
- Ambiguous references to parent/legacy entities without context.
- Excessive internal history not relevant to client outcomes.
- Placeholder biographies and stock claims without evidence.

### Subdomain recommendation
- Keep as `https://www.cyberfyx.net/about-us/`
- Optional future split only if investor/press relations expand (e.g., `company.cyberfyx.net`).

---

## 3) Our Services

### Page goal
Help buyers understand each service quickly and request the next step.

### Relevant content to include
- **Service taxonomy by outcome**, not just category names:
  - Assess (VAPT, risk assessments, posture review)
  - Comply (ISO/PCI/DPDPA readiness)
  - Protect (endpoint, hardening, monitoring)
  - Respond (incident readiness / IR support)
  - Improve (training and maturity programs)
- **Each service page format**:
  1. Business problem,
  2. Solution scope,
  3. Deliverables,
  4. Timeline,
  5. Ideal customer profile,
  6. CTA.
- **Cross-links** between services and industries.
- **Proof blocks**: case snippets, frameworks, measurable outcomes.

### Irrelevant content to remove
- One-page service dumping with no prioritization.
- Tool names without explaining business impact.
- Overuse of acronyms without plain-English explanation.

### Subdomain recommendation
- Keep under root path for SEO authority:
  - `https://www.cyberfyx.net/our-services/`
  - `https://www.cyberfyx.net/cybersecurity/`
  - `https://www.cyberfyx.net/it-security/` etc.
- Use a subdomain only if launching a distinct SaaS portal/product.

---

## 4) Industries

### Page goal
Show industry-specific relevance and compliance competence.

### Relevant content to include
- Individual industry pages for top target verticals:
  - Healthcare
  - Banking/Financial Services
  - Government/Public Sector
  - Manufacturing
  - Retail/E-commerce
  - IT/Technology
- For each industry page include:
  - Threat patterns,
  - Typical compliance/regulatory obligations,
  - Common risk scenarios,
  - Relevant Cyberfyx services,
  - One mini case example,
  - Industry-specific CTA.
- Fix and replace any staging links with production URLs.

### Irrelevant content to remove
- Generic copy reused across all industry pages.
- Lists of industries with no context or links.
- Broken links to temporary/staging domains.

### Subdomain recommendation
- Keep as directory model:
  - `https://www.cyberfyx.net/industries/healthcare/`
  - `https://www.cyberfyx.net/industries/bfsi/`
- Avoid one-subdomain-per-industry until scale requires it.

---

## 5) Careers

### Page goal
Attract qualified talent and create a frictionless application journey.

### Relevant content to include
- **Employer value proposition** focused on mission and growth.
- **Open roles** with structured details:
  - level,
  - location,
  - required certifications,
  - key responsibilities,
  - outcomes expected in first 90 days.
- **Hiring process section** (screening → interview → decision timeline).
- **Learning culture**: certifications, mentorship, client exposure.
- **Equal opportunity statement** and workplace standards.

### Irrelevant content to remove
- Duplicate careers pages with overlapping purposes.
- Outdated role postings.
- Generic HR filler content unrelated to security practice work.

### Subdomain recommendation
- Primary: `https://www.cyberfyx.net/job-openings/`
- If ATS integration is adopted, map branded subdomain: `jobs.cyberfyx.net`.

---

## 6) Contact Us

### Page goal
Convert visitors to qualified leads and support requests with quick routing.

### Relevant content to include
- **Short, high-intent form**:
  - Name,
  - Work email,
  - Company,
  - Requirement,
  - Estimated timeline.
- **Contact routing** options:
  - Sales inquiries,
  - Partnership inquiries,
  - Existing client support.
- **Response commitment** (e.g., within 1 business day).
- **Location and operating hours**.
- **Data privacy notice** for form submissions.

### Irrelevant content to remove
- Long forms with excessive mandatory fields.
- Fake/placeholder contact details.
- Unclear submission status (no confirmation state).

### Subdomain recommendation
- Keep contact page on primary domain: `https://www.cyberfyx.net/contact-us/`
- Optional support function on `support.cyberfyx.net` if helpdesk is distinct.

---

## Additional Content Recommendations (Important)

### A) Case Studies Hub (High priority)
Add 4–8 concise case studies across core verticals and service lines:
- Challenge,
- Approach,
- Controls implemented,
- Result/impact.

### B) Insights / Blog Rebuild (High priority)
Replace template/dummy posts with cybersecurity-native topics:
- DPDPA readiness checklists,
- ISO 27001 implementation mistakes,
- Ransomware response playbooks,
- Endpoint hardening in hybrid work environments,
- Third-party/vendor risk management.

### C) Downloadable Assets (Medium priority)
Lead magnets for conversion:
- Security maturity checklist,
- Incident response plan template,
- PCI DSS readiness self-assessment,
- Board-level cyber risk briefing one-pager.

### D) FAQ Rebuild (Medium priority)
Create a genuine cybersecurity FAQ (pricing model, project duration, certification support, readiness audits, managed vs consulting).

### E) Proof & Trust Layer (High priority)
- Client logos (where permitted),
- Partner badges,
- Certifications,
- Leadership speaking engagements,
- Compliance frameworks supported.

---

## Subdomain Strategy (Final Recommendation)

### Keep on main domain path (default)
- Home, About, Services, Industries, Careers, Contact, Blog

### Use subdomains only for distinct systems
- `support.cyberfyx.net` → ticketing/helpdesk
- `portal.cyberfyx.net` → client portal/dashboard
- `jobs.cyberfyx.net` → ATS-hosted job system
- `academy.cyberfyx.net` → learning portal (if training platform expands)

### Why this model
- Better SEO consolidation,
- Stronger trust continuity,
- Simpler analytics and conversion tracking,
- Lower content governance overhead.

---

## Content Governance Model

### Ownership
- Marketing: page messaging, editorial calendar, conversion assets.
- Cyber/Delivery SMEs: technical validation, compliance accuracy.
- Leadership: final approval for positioning and public claims.

### Publishing cadence
- Monthly: 2 insight articles + 1 case study update.
- Quarterly: page performance and conversion review.
- Bi-annual: full content quality and relevance audit.

### Core quality checklist (before publish)
- Is the content cybersecurity-relevant?
- Is every claim supported by proof/example?
- Is there a clear CTA?
- Are links and forms working?
- Is page language clear to both technical and business audiences?

---

## 30-60-90 Day Rollout Plan

### First 30 days
- Remove/redirect irrelevant template pages.
- Rewrite Home, About, Contact for conversion clarity.
- Fix staging/broken links on Industries.

### Day 31–60
- Rebuild Services with consistent service-page template.
- Launch 3 industry pages with tailored content.
- Publish first 4 real blog/insight posts.

### Day 61–90
- Launch case study hub and downloadable resources.
- Improve Careers experience and role content.
- Implement analytics dashboard for CTA and form conversion.

---

## Final Team Presentation Summary
Cyberfyx should prioritize **content credibility, buyer clarity, and controlled IA simplification**. The current website has strong service intent but loses trust through outdated template leftovers and inconsistent content quality. A focused rewrite of the six core pages, supported by case studies, industry relevance, and a conservative subdomain strategy, will significantly improve perceived authority and lead conversion.

