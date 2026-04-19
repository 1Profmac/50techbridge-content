# Workforce Decision Maker Nurture Sequence
## Mailchimp automation — Learn More Technologies / 50+TechBridge

**Audience:** Workforce managers, HR leaders, workforce board members, MBE council leaders, training-eligible org decision makers
**Goal:** Cold contact → trust → 15-minute call → workforce contract or WIOA enrollment
**Length:** 7 emails over 60 days
**Conversion target:** 5-10% book a call by Email 6

---

## Mailchimp Setup (do this first)

### 1. Create the Audience
- **Audience name:** LMT Workforce Decision Makers
- **From name:** Brian McKinney
- **From email:** brian@learnmoretechnologies.com
- **Default subject prefix:** none
- **Reply-to:** brian@learnmoretechnologies.com
- **Address (CAN-SPAM required):** [LMT business address]

### 2. Set up Tags (segmentation)

Tag every contact with these on import:

| Tag category | Values |
|---|---|
| **Source** | `linkedin` / `event` / `referral` / `cold-research` / `inbound-form` |
| **Org type** | `workforce-board` / `tx-state` / `large-employer` / `nonprofit` / `mbe-org` / `community-college` / `chamber` / `government` |
| **Region** | `austin` / `dallas` / `houston` / `san-antonio` / `other-tx` / `other` |
| **Tier** | `tier-1` / `tier-2` / `tier-3` |
| **Openness rating** | `hot-5` / `warm-4` / `receptive-3` / `cold-2` / `skip-1` |
| **Status** | `nurture-active` / `engaged` / `meeting-scheduled` / `closed-won` / `closed-lost` / `unsubscribed` |

### 3. Custom Merge Fields

Add these to the audience settings:

| Field name | Tag | Type |
|---|---|---|
| First Name | FNAME | text |
| Last Name | LNAME | text |
| Title | TITLE | text |
| Organization | ORG | text |
| City | CITY | text |
| Source Hook (specific thing they care about) | HOOK | text |
| LinkedIn URL | LINKEDIN | text |
| Phone | PHONE | text |

### 4. Create the Automation
- Mailchimp → Automations → Customer Journeys → Create new
- **Trigger:** Tag added "nurture-active"
- **Goal:** Tag added "meeting-scheduled" (exits the journey)
- Add the 7 emails below as steps with the wait times specified

### 5. Important Mailchimp settings
- ✅ Personalize with merge tags
- ✅ Track opens and clicks
- ✅ Send at recipient's local time (if possible)
- ✅ A/B test subject lines on Email 1 and Email 6 (highest impact)
- ✅ Suppress sends on weekends (Sat/Sun) — these are B2B
- ✅ Default send time: Tuesday or Wednesday 9:00 AM Central

---

## The 7 Emails

### EMAIL 1 — Day 0 (immediately after tag added)

**Subject:** $850 billion. Every year. Gone.
**Preheader:** And the reason will sound familiar.
**Send time:** Tuesday or Wednesday 9 AM CT

```
Hi *|FNAME|*,

$850 billion. That's what U.S. organizations lose every year by ignoring
their experienced workers.

Not because of bad strategy. Not because of market conditions. Because of
one assumption nobody questions: "Older workers can't keep up with
technology."

I built Learn More Technologies to prove that wrong. We've trained 347
adults 50+ in AI and digital skills with a 3X industry completion rate
and a 74% confidence increase.

Here's the 4-minute video that lays out the problem:
[link to YouTube Part 1]

I'll be sending you a few more pieces of this story over the next few
weeks. If anything resonates — or if you'd rather not hear from me — just
reply. I read every one.

Brian McKinney
Founder, Learn More Technologies (MBE-certified)
Austin, TX

P.S. If your organization is thinking about how to retain experienced
talent or upskill workers 50+, that's exactly what we're here for.
learnmoretechnologies.com/workforce
```

**Why this email works:**
- Stat-led subject line (curiosity gap)
- Immediate value, no ask
- Single link, single CTA
- Permission language at the end ("if you'd rather not hear from me")
- P.S. plants the seed for what's coming

---

### EMAIL 2 — Day 3

**Subject:** Workers 55-64 stay 10.1 years. Workers 25-34 stay 3 years.
**Preheader:** That's not loyalty. That's math.

```
Hi *|FNAME|*,

Workers 55-64 stay an average of 10.1 years at their employer.

Workers 25-34 stay 3 years.

That's not loyalty. That's math.

Here's the part that most workforce leaders miss: upskilling an existing
employee costs about 6X less than hiring externally. Yet U.S.
organizations spend half as much training workers over 55 as they do
training workers under 35.

We're paying premium prices to replace people who would have stayed —
and underinvesting in the people who already chose to stay.

I made a 3-minute video about this:
[link to YouTube Part 2]

If you're doing workforce planning right now, this is the math your
budget conversation should start with.

Brian
```

**Why this email works:**
- Math the recipient can't argue with
- Reframe ("loyalty vs math")
- Builds on Email 1 without repeating it
- Single specific CTA (the video)
- No ask, no pressure

---

### EMAIL 3 — Day 7

**Subject:** 347 Pioneers. 3X the industry completion rate.
**Preheader:** And one short story you should hear.

```
Hi *|FNAME|*,

I've been telling you stats. Let me tell you a story instead.

A 58-year-old former retail manager came to one of our cohorts last year.
She had been laid off after 22 years and told by an outplacement firm that
her best bet was to apply for warehouse jobs.

After 8 weeks in our program, she's now using AI tools to do market
research as a freelance consultant — billing $40/hour for work she didn't
know she could do.

She's one of 347 Pioneers we've trained. Our completion rate is 3X the
industry average. 74% report significantly more confidence with technology.
23 organizations have invited us in to teach their members and constituents.

We're MBE-certified. We're based in Austin. We work with workforce boards,
employers, faith communities, libraries, and senior centers.

If you'd like to see what our program looks like, here's a 2-page overview:
[link to LMT capability sheet PDF]

No call needed. Just take a look when you have 5 minutes.

Brian
```

**Why this email works:**
- Story instead of stats (different format)
- Concrete, specific (58-year-old, 22 years, $40/hour)
- Proof points repeated for repetition's sake
- Capability sheet download (low-friction)
- Explicit "no call needed" reduces pressure

---

### EMAIL 4 — Day 14

**Subject:** Your 50+ workers aren't the problem. Your training is.
**Preheader:** A contrarian take you can argue with.

```
Hi *|FNAME|*,

Here's a take most workforce people don't want to hear:

Your 50+ workers are not the problem.

Your training is.

When 60% of older workers fail a digital skills program, the conclusion
shouldn't be "older workers can't learn." It should be "this program is
designed wrong."

The same people who "can't keep up" with a 12-week generic AI course can
finish our program at 3X the industry completion rate. We didn't change
the people. We changed the training.

This is the contrarian frame I've been pushing in my $850 Billion Series:

[link to LinkedIn Article or full series]

If you're sending experienced workers to programs designed for 25-year-olds
and wondering why retention is down, that's the gap. We exist to close it.

I'd love your reaction — agree or disagree, I want to hear it. Just hit
reply.

Brian
```

**Why this email works:**
- Contrarian hook (sparks reaction)
- Reframes the problem
- Asks for reply (engagement = future deliverability)
- Soft CTA, no ask for time

---

### EMAIL 5 — Day 21

**Subject:** How [Partner Org Name] retained 12 experienced workers in 90 days
**Preheader:** A specific case, with the math.

```
Hi *|FNAME|*,

A few months ago, a community organization in Austin came to us with a
problem: they had 12 experienced staff members — average age 56 — who
were struggling to use the new digital case management system their funder
required.

The org's options looked expensive: retrain externally ($X each), or lose
them and hire replacements ($Y each). Total cost either way: ~$[number].

Instead, they enrolled all 12 in our 6-week program.

90 days later:
✅ All 12 completed the training
✅ All 12 successfully adopted the new system
✅ Confidence scores up 80% on average
✅ Total cost: ~$[number] (about [X]% of the alternative)
✅ Zero turnover among the cohort

That's the kind of outcome that makes a workforce manager's quarter.

If you're facing a similar situation — dispersed adoption, training that's
not landing with experienced staff, retention pressure — I'd love to walk
through what a custom cohort might look like for your organization.

15 minutes, no slides:
[Calendly link: calendly.com/brianmckinney/new-meeting]

Brian
```

**Why this email works:**
- Concrete case study with specific math
- Aligns to recipient's likely problem
- First explicit call-to-book CTA
- Low friction (15 min, no slides)
- Use a real Pioneer story (just anonymize)

⚠️ **Customize before sending:** Use a real partner org and real numbers. If you don't have a clean case study yet, write a generic version and replace it as soon as you have one.

---

### EMAIL 6 — Day 28

**Subject:** Ready to talk about your workforce?
**Preheader:** 15 minutes. 3 questions. No slides.

```
Hi *|FNAME|*,

I've sent you a few pieces of the LMT story over the past month. If you've
read any of them, thank you.

Here's where I am: I'm looking for 3 workforce decision makers in Texas
who want to be early partners in scaling adult digital skills training in
2026.

If that might be you, I'd like 15 minutes of your time to ask three
questions:

1. What's your biggest workforce challenge with experienced staff right now?
2. What have you tried — and what hasn't worked?
3. If we could solve one thing for you in the next 90 days, what would it
   be?

That's the whole call. No slides. No pitch deck. Just a conversation.

Pick a time that works for you:
[Calendly: calendly.com/brianmckinney/new-meeting]

If now isn't the right time, just hit reply with "later" and I'll check
back in 60 days. No hard feelings.

Brian
```

**Why this email works:**
- Direct ask, finally
- Specific 3-question framework (lowers anxiety)
- Scarcity ("3 partners") without being manipulative
- Permission to defer ("just reply 'later'")
- Easy out builds trust

---

### EMAIL 7 — Day 60 (long-term nurture, runs only if no meeting scheduled)

**Subject:** Quick check-in — anything new in your workforce planning?
**Preheader:** And one new data point you can use.

```
Hi *|FNAME|*,

Wanted to circle back briefly.

I know workforce planning happens in cycles. The conversation that doesn't
fit in April might be exactly the right conversation in July.

One thing that's changed since we last connected: [insert most recent
proof point — new partner, new outcome, new policy change in WIOA, new
LMT graduate story].

If anything has shifted on your end — new initiative, new RFP, a workforce
challenge that came up — I'm still here. Hit reply or grab time:

[Calendly: calendly.com/brianmckinney/new-meeting]

If you want to stop hearing from me entirely, no problem — there's an
unsubscribe link below and I won't be offended.

Brian

P.S. We just shipped Part 2 of our $850 Billion Series on YouTube and
LinkedIn. If you missed it, the retention math is in the first 90 seconds:
[link]
```

**Why this email works:**
- Low-pressure check-in
- New data hook
- Explicit unsubscribe permission (deliverability hygiene)
- One last CTA + proof point in P.S.

---

## Sequence after Email 7

If still no meeting:
- Move to **`tier-3-quarterly`** tag
- Quarterly newsletter only (no nurture sequence)
- Move back to nurture sequence if they engage with newsletter or visit website

If meeting scheduled:
- Tag updated to **`meeting-scheduled`**
- Sequence stops automatically (Mailchimp goal)
- Manual follow-up by Brian

If they reply at any point:
- Pause the sequence manually
- Brian replies personally
- Resume only if they explicitly say "keep sending"

---

## Tracking metrics (review weekly)

| Metric | Target | Action if missed |
|---|---|---|
| Email 1 open rate | 35%+ | Test subject line variants |
| Email 1 click rate | 8%+ | Check video link, retest preheader |
| Email 2-4 open rate | 25%+ | List quality issue or sender reputation |
| Email 5 click rate (book call CTA) | 5%+ | Refine the case study |
| Email 6 booking rate | 3-5% | This is your main conversion metric |
| Unsubscribe rate per email | <1% | If higher, sequence is too aggressive |
| Reply rate (any email) | 2-4% | Replies = deliverability gold |

---

## Variants by segment (build later)

Once the base sequence is running, build segment-specific variants:

### Variant A: Workforce Boards (TWC, Workforce Solutions)
- Email 5 case study should reference a fellow workforce board's outcome
- Email 6 should mention WIOA ETPL eligibility / partner status
- More formal tone

### Variant B: Large Employer HR Leaders (Dell, AT&T, USAA, H-E-B)
- Email 5 case study should reference an enterprise outcome
- Email 6 should reference cost-per-employee math
- Emphasize ROI

### Variant C: MBE Councils
- Lean into MBE-to-MBE connection
- Reference minority business support angle
- Different CTAs (community partnership, joint events)

### Variant D: Community Colleges & Nonprofits
- Cohort partnership angle, not contract
- Lower friction (no budget conversation)
- Joint grant opportunities

---

## When to send vs. pause the sequence

**Always pause the sequence if:**
- They reply (Brian responds personally)
- They book a call
- They unsubscribe
- They explicitly ask to slow down

**Always continue the sequence if:**
- They open emails but don't click (they're paying attention)
- They click but don't reply (they're researching)
- They go silent for a few emails (silence isn't rejection)

**Restart the sequence if:**
- They re-engage after dropping off (clicked a newsletter, downloaded a resource)
- They change roles or organizations
- Major LMT news (book launch, big speaking gig, new partner)

---

## Compliance notes

- ✅ CAN-SPAM compliant: physical address in footer, unsubscribe link, no deceptive subject lines
- ✅ TCPA: not applicable (email, not SMS)
- ✅ GDPR: not required for US-based audience but good practice
- ⚠️ **Texas business email**: ensure LMT's CAN-SPAM compliant address and contact info appear in every email
- ⚠️ **Mailchimp Acceptable Use**: avoid bought lists, don't mass-import contacts who didn't opt in. Use only people who:
  - Connected with you on LinkedIn first
  - Met you in person and gave you a card
  - Filled out the lead form on /workforce
  - Were referred by name from a current contact

**Do NOT** import the prospect research dossiers as cold contacts to Mailchimp without prior contact. That's both an Acceptable Use violation and bad relationship hygiene.

---

## How this fits with the rest of the LMT marketing system

| System | Role |
|---|---|
| Marketing Morning Routine (daily trigger) | Adds 5 prospects/day to LMT's targeting sheet, drafts comment-first warm-ups |
| `/prospect` skill | Produces deep dossier per prospect; identifies if they're list-ready |
| Decision-Maker Access Playbook | The 16 channels for warming people BEFORE they get added to this sequence |
| Social Strategy Review | Builds the inbound traffic that fills the lead form |
| **This nurture sequence** | The middle layer — converts warmed contacts into booked calls |
| WIOA ETPL Application Packet | The big-ticket conversion path for workforce boards |

Run all five together and the system feeds itself. Sleep well.
