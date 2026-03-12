# Cyberfyx Website Content Report

## Executive Note
We are ready to publish this as our internal-facing content direction report.

Over the past review cycle, we audited the current Cyberfyx website content, identified what is helping us, and documented what is diluting trust. This report reflects our team consensus on what to keep, what to remove, and how to structure content and subdomains so the site feels credible, clear, and conversion-ready.

---

## Quick References (Full Links)

### Live website references
- Home: https://www.cyberfyx.net/
- About Us: https://www.cyberfyx.net/about-us/
- Our Services: https://www.cyberfyx.net/our-services/
- Cybersecurity: https://www.cyberfyx.net/cybersecurity/
- IT Security: https://www.cyberfyx.net/it-security/
- Endpoint Management: https://www.cyberfyx.net/endpoint-management/
- Industries: https://www.cyberfyx.net/industries/
- Careers: https://www.cyberfyx.net/job-openings/
- Contact Us: https://www.cyberfyx.net/contact-us/

### Repository references (update with final repo URL before publication)
> Replace `<ORG>` and `<REPO>` once this report is published publicly.

- Report file: https://github.com/<ORG>/<REPO>/blob/main/draft-report.md
- Home scrape reference: https://github.com/<ORG>/<REPO>/blob/main/raw_scraped_data/home.txt
- About scrape reference: https://github.com/<ORG>/<REPO>/blob/main/raw_scraped_data/about-us.txt
- Services scrape reference: https://github.com/<ORG>/<REPO>/blob/main/raw_scraped_data/our-services.txt
- Industries scrape reference: https://github.com/<ORG>/<REPO>/blob/main/raw_scraped_data/industries.txt
- Careers scrape reference: https://github.com/<ORG>/<REPO>/blob/main/raw_scraped_data/job-openings.txt
- Contact/Get Quote scrape reference: https://github.com/<ORG>/<REPO>/blob/main/raw_scraped_data/get-a-quote.txt

---

## What We Completed

### Audit scope
We reviewed the core website content and mapped it against the expectations of a cybersecurity-first brand.

### What we found
1. Our core service intent is strong and technically credible.
2. Several pages still carry legacy/template content that weakens trust.
3. Industry and insight content needs stronger depth and better narrative quality.
4. A main-domain-first architecture is still the best option for SEO and user confidence.

---

## Final Information Architecture We Recommend

### Core navigation
- Home
- About Us
- Our Services
- Industries
- Careers
- Contact Us

### Supporting sections
- Leadership Team (nested under About)
- Case Studies
- Insights / Blog
- Compliance Resources / Downloads
- Client Success / Testimonials

---

## 1) Home

### Our intent
We use this page to create immediate trust, communicate our value clearly, and move visitors to action.

### Relevant content (keep/add)
- A confident and plain-language hero statement.
- Primary CTA above the fold: **Book a Security Consultation**.
- Secondary CTA: **Get a Quote** or **Talk to an Expert**.
- Service snapshot tiles (Cybersecurity, IT Security, Endpoint Management, Training).
- Trust signals: certifications, leadership credibility, years of combined experience.
- Industry highlights with direct links.
- Outcome-based proof points (audit support, assessment volume, remediation impact).
- Latest insights to show active expertise.

### Irrelevant content (remove/avoid)
- Long generic intros with no business outcome.
- Repeated paragraphs copied across multiple pages.
- Legacy logistics-theme language or visuals.
- Conflicting, duplicate, or broken CTAs.

### Subdomain decision
- Keep Home on main domain: https://www.cyberfyx.net/
- No Home subdomain.

---

## 2) About Us

### Our intent
We use this page to humanize the brand and reinforce confidence in our delivery maturity.

### Relevant content (keep/add)
- Clear company story: why we exist and what problem we solve.
- Mission, vision, values connected to client outcomes.
- Leadership profiles with meaningful credentials.
- Delivery model: advisory + implementation + managed support.
- One clear statement on KRISH CORP relationship (if applicable).
- Company milestones that matter to clients and partners.

### Irrelevant content (remove/avoid)
- Ambiguous legacy references without context.
- Internal details that do not support buyer confidence.
- Placeholder bios or claims we cannot validate.

### Subdomain decision
- Keep About on main path: https://www.cyberfyx.net/about-us/
- Consider a company subdomain only if investor/press content grows materially.

---

## 3) Our Services

### Our intent
We use Services to make buying easier: fast understanding, clear scope, clear next step.

### Relevant content (keep/add)
- Services grouped by business outcome:
  - **Assess** (VAPT, posture review, risk assessment)
  - **Comply** (ISO, PCI DSS, DPDPA readiness)
  - **Protect** (endpoint and control hardening)
  - **Respond** (incident readiness and response support)
  - **Improve** (training and maturity uplift)
- Consistent service-page structure:
  1. Business challenge
  2. Scope and approach
  3. Deliverables
  4. Typical timeline
  5. Ideal customer profile
  6. CTA
- Cross-links to relevant industry pages.
- Proof modules with measurable outcomes.

### Irrelevant content (remove/avoid)
- One long undifferentiated services page.
- Tool/vendor names without business explanation.
- Unexplained jargon and acronym overload.

### Subdomain decision
- Keep services on primary path:
  - https://www.cyberfyx.net/our-services/
  - https://www.cyberfyx.net/cybersecurity/
  - https://www.cyberfyx.net/it-security/
- Use a subdomain only for a standalone product platform.

---

## 4) Industries

### Our intent
We use industry pages to show we understand sector-specific threats, controls, and compliance realities.

### Relevant content (keep/add)
- Priority pages:
  - Healthcare
  - Banking / Financial Services
  - Government / Public Sector
  - Manufacturing
  - Retail / E-commerce
  - IT / Technology
- Standard block structure for each industry page:
  - Threat patterns
  - Regulatory/compliance expectations
  - Typical risk scenarios
  - Mapped Cyberfyx service fit
  - One short case example
  - Industry-specific CTA
- Replace all staging links with production links.

### Irrelevant content (remove/avoid)
- Generic copy pasted across industries.
- Empty industry lists with no practical value.
- Broken or temporary/staging URLs.

### Subdomain decision
- Keep industry pages on primary path:
  - https://www.cyberfyx.net/industries/
  - Example: https://www.cyberfyx.net/industries/healthcare/
- Avoid one-subdomain-per-industry.

---

## 5) Careers

### Our intent
We use Careers to attract high-quality talent while keeping the application path simple and transparent.

### Relevant content (keep/add)
- Strong employer value proposition aligned to mission.
- Active role descriptions with scope and expectations.
- Clear hiring process and response timelines.
- Learning and growth narrative (certifications, mentoring, exposure).
- Equal opportunity and workplace culture standards.

### Irrelevant content (remove/avoid)
- Duplicate career pages.
- Expired openings.
- Generic HR text disconnected from cybersecurity roles.

### Subdomain decision
- Keep Careers on main path: https://www.cyberfyx.net/job-openings/
- If an ATS is introduced, we can map: https://jobs.cyberfyx.net/

---

## 6) Contact Us

### Our intent
We use Contact to capture intent, route requests correctly, and shorten response cycles.

### Relevant content (keep/add)
- Short, conversion-friendly form:
  - Name
  - Work email
  - Company
  - Requirement
  - Timeline
- Inquiry routing: Sales, Partnerships, Support.
- Response commitment (SLA language).
- Office/location and working hours.
- Privacy assurance for form submissions.

### Irrelevant content (remove/avoid)
- Overlong forms with unnecessary required fields.
- Placeholder contact details.
- Missing success/confirmation message after form submit.

### Subdomain decision
- Keep Contact on primary path: https://www.cyberfyx.net/contact-us/
- Support subdomain only if helpdesk tooling is separate: https://support.cyberfyx.net/

---

## Additional Content We Should Publish

### 1) Case Studies Hub (High priority)
We should publish 4–8 concise case studies covering challenge, approach, controls, and measurable outcomes.

### 2) Insights / Blog Rebuild (High priority)
We should replace template posts with practical cybersecurity topics:
- DPDPA readiness checklist
- ISO 27001 implementation pitfalls
- Ransomware preparedness and response
- Endpoint hardening in hybrid work
- Third-party risk controls

### 3) Downloadable Assets (Medium priority)
We should create lead-generation assets:
- Security maturity checklist
- Incident response template
- PCI DSS readiness worksheet
- Board-level cyber risk one-pager

### 4) FAQ Rebuild (Medium priority)
We should launch a practical FAQ that answers real buyer questions on pricing models, timelines, standards, and support scope.

### 5) Proof Layer (High priority)
We should strengthen trust with:
- Approved client logos
- Partner badges
- Certifications
- Leadership speaking credentials
- Supported compliance frameworks

---

## Final Subdomain Strategy

### Keep on main domain path by default
- Home, About, Services, Industries, Careers, Contact, Blog.

### Use subdomains only for distinct systems
- Support: https://support.cyberfyx.net/
- Portal: https://portal.cyberfyx.net/
- Jobs (ATS): https://jobs.cyberfyx.net/
- Academy (future training platform): https://academy.cyberfyx.net/

### Why this is the right model for us
- Consolidates SEO authority.
- Preserves one consistent trust experience.
- Simplifies analytics and attribution.
- Reduces governance and maintenance overhead.

---

## Content Governance

### Ownership
- Marketing owns messaging, editorial flow, and conversion assets.
- Cyber/Delivery SMEs validate all technical and compliance content.
- Leadership approves external claims and positioning.

### Publishing rhythm
- Monthly: 2 insights + 1 case update.
- Quarterly: conversion and content performance review.
- Bi-annual: full relevance and quality audit.

### Pre-publish checklist
- Is this cybersecurity-relevant and audience-appropriate?
- Are all claims backed by proof or examples?
- Is the CTA clear and page-specific?
- Are links and forms functional?
- Is the language understandable to both technical and business readers?

---

## Final Team Summary
We have completed the content planning baseline for all six core pages and aligned on a practical subdomain model. This version is polished for publication and presentation, while still actionable for immediate implementation.
