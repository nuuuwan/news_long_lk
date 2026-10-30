# Insurers’ AI Ambitions Are Outpacing Their Data

[https://hbr.org/sponsored/2026/10/insurers-ai-ambitions-are-outpacing-their-data](https://hbr.org/sponsored/2026/10/insurers-ai-ambitions-are-outpacing-their-data)

*04:11 PM, Thursday, October 29, 2026*

By Vibhor Gupta and Manish Sood

An AI agent reviews a family’s household insurance claim and automatically denies it due to a lapse in coverage. But the customer had renewed the policy two days before the accident, and that update somehow hadn’t made it into the system.

This kind of hypothetical situation shows how quickly an AI decision can go wrong when the data behind the decision is incomplete, with real consequences for the customer.

Before it can trust an AI system to approve a claim, detect fraud, or write policies, an organization has to be confident that its data is accurate, current, and governed. Otherwise, the AI’s recommendation is simply a plausible guess.

That confidence is proving hard to come by. And many insurers are moving faster than their data can support.

Insurance carriers are moving quickly to put AI to work, but their data often isn’t ready to support the faster decisions they’re asking it to make.

More than half of insurers are using AI for fraud detection and customer servicing, and almost half have fully deployed it for actuarial and underwriting solutions, according to a 2026 study by EXL.

The appeal is easy to see. AI can flag a suspicious claim in seconds, assemble the context an underwriter would otherwise spend hours gathering, and tackle routine tasks so people can focus on the decisions that require strategic oversight and human judgment.

However, 92% of insurers say their data is a challenge to AI success, the study found, and data silos are a bigger barrier in the insurance sector than in any other industry surveyed.

This is a pattern we have both seen firsthand. One of us spent years consolidating and governing customer data at Shelter Insurance before extending that foundation to AI, and the other has spent a decade building Reltio, the infrastructure that insurers and other organizations depend on to get their data AI-ready.

The gap between what AI can do and what insurers trust it to do can almost always be traced back to the same root cause: No matter how sophisticated the model, the underlying data is simply not sufficient.

Data First, Transformation Second

At Shelter Insurance, we made an early decision that ran counter to how most insurance transformations happen. We were midway through moving off a legacy mainframe system and onto a modern core insurance platform.

The standard approach would have been to migrate our existing data as is, inconsistencies and all, and clean it up afterward. Instead, we consolidated and governed our customer data first, using Reltio to build a single source of truth for every customer before we touched the core transformation at all.

That decision also meant taking on work most carriers hand off entirely. Our systems integrator’s standard playbook was to migrate legacy data directly onto the new platform. We instead migrated from our already-governed data environment onto the new platform.

Doing it this way meant Shelter, not a third party, could make the hard calls about what counted as the correct version of a customer record, who owned that decision, and how to handle exceptions. We completed the full transformation of our largest line of business in 18 months, on time and under budget—a timeline that would have been difficult to imagine if we’d needed to reconcile data-quality problems in the middle of a core systems cutover. Getting the data right first made moving fast possible.

Human Judgment at Scale

Insurance data doesn’t stay accurate on its own. Customers relocate, renew coverage through various channels, and update details in ways that don’t always sync cleanly across systems. At Shelter, we found more than 100,000 records with conflicting information across policies—often subtle inconsistencies that can remain undetected for years until they surface in a claim.

Rather than using AI to decide which version of a record was correct, we built an AI agent to surface discrepancies to the people best positioned to resolve them. In most cases, that was the human agent at the local agency closest to the customer, who has the context to know which record is correct. That person reviewed the flagged conflict and confirmed the correct information, and that update flowed back through our systems.

The distinction matters. We didn’t ask AI to decide whether the data was correct but to identify where the organization needed human judgment. That only worked because we had already organized and governed the underlying data.

We rolled out this feature to staff across more than 2,700 agencies, and the same pattern holds at each one: AI surfaces the exception, a person makes the call, and the system learns from that decision and gets more reliable for the next time.

Governance Is Leadership’s Responsibility

This approach only works with a formal structure behind it. Shelter built its AI governance platform in-house with intake, automated vendor risk scoring, committee review, guardrails, and ongoing monitoring—all evaluated against five regulatory frameworks.

AI governance isn’t a function for executives to delegate to IT or compliance teams and check in on quarterly. It’s an enterprise leadership responsibility on par with any other capability that determines how much authority the business is willing to extend. For Shelter, operating across 22 states adds real regulatory weight to that structure, but the goal was never mere compliance. It was to have a repeatable, scalable way to decide which uses of AI were appropriate and how much autonomy it could be trusted to exercise.

A Practical Test for Granting AI Authority

Before letting an agent act, we ask five questions:

Does it know which customer, policy, or claim it’s dealing with?

Does it have the relevant history, relationships, and permissions?

Can it show why it reached its conclusion?

Is it authorized to take this action, or does it need human sign-off?

Can a person review, override, and improve the result?

An agent that can’t clear all five criteria isn’t ready for authority, no matter how capable the underlying model is.

Build the Foundation First

Insurance carriers are under immense pressure to show AI progress now. But the organizations scaling AI responsibly now or in the coming years will likely be the ones that did the less visible work of organizing their data first.

As AI takes on more consequential decisions, the quality of an insurer’s data becomes inseparable from its ability to keep its promises to customers. The fastest path to autonomy is doing the foundational work now.

Vibhor Gupta is Vice President of Enterprise Data at Shelter Insurance.

Manish Sood is the founder and CEO of Reltio.

Learn how Reltio helps insurers build the trusted data foundation for reliable, responsible AI.

