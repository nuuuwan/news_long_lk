# Generative AI for Security: Harnessing Amazon Bedrock for Customer Impact

## Summary 🤖

Facts:

- Cybercriminals are increasingly using Generative AI (GenAI) tools to carry out ransomware attacks and other advanced breaches rapidly and efficiently.
- Generative AI can also be used defensively, to automate the investigative process of security alerts for businesses.
- The first step in GenAI security involves creating an instrumented infrastructure that offers visibility into all potential threat areas, such as ransomware.
- Effective security requires three lines of defence: attack detection, investigation, and response. Prevention and detection measures are not adequate as they may be bypassed by threat actors.
- Vulnerability reduction requires robust data infrastructure where information is centralized, indexed and readily available. This should contain data from diverse sources including user audit records, network connections, business application telemetry and security alerts.
- To keep up with the speed of ransomware, all three components of security (detection, investigation and response) should be automated, with GenAI handling the major portion of the investigative load.
- Consulting firm Cyberuptive used GenAI from Trellix Wise to reduce response times, increase incident resolution efficiency and enhance their overall security posture.
- Amazon Bedrock is a service that provides high-performing foundation models from leading AI companies. It includes all the necessary features to build generative AI applications with security, privacy, and responsible AI.

Opinions:

- Security operations staff feeling helpless against the increasing threat from AI-enabled cyberattacks is a significant challenge.
- The potential of GenAI to enhance security is touted as high, a view shared by 91% of CISOs according to a study by Trellix.
- The article suggests that automating investigations with Generative AI using a predefined list of vital questions can help connect strategic defense components.
- According to the authors, GenAI can not only ask these important investigative questions but also make inferences, much like a human analyst.
- The article expresses the opinion that using GenAI can significantly augment an organization's cyber defence strategy by giving them the means to match the sophistication of modern cybercriminals.

## Follow-up Questions 🤖

1. What are some examples of generative AI (GenAI) used by cybercriminals, and how does it expedite ransomware installation?
2. How does GenAI assist understaffed security teams in handling such a vast array of threats?
3. The article mentions a study that suggests 91% of CISOs are excited about the prospects and opportunities GenAI and AI will bring to their organization. What are some specific areas these CISOs are looking forward to improving or transforming with AI technology?
4. How does the progression of detection, investigation, and response work in a GenAI secured environment? 
5. Could you elaborate on the concept of "pre-built scaffolding of investigations" in AI-powered cybersecurity?
6. How does the AI-powered system infer data and make human-like judgments from the trainable data?
7. The example of Cyberuptive depicts the successful implementation of GenAI. Can you provide more such successful stories of GenAI utilization in real-world scenarios?
8. How does the integration of Amazon's Bedrock enhance the performance of Trellix's GenAI? 
9. How would one rate the effectiveness of using generative AI systems compared to traditional cyber-security methods?
10. Could the adoption of GenAI for cybersecurity be a potential solution for underfunded security operations?

## Full Text

[https://hbr.org/sponsored/2024/06/generative-ai-for-security-harnessing-amazon-bedrock-for-customer-impact](https://hbr.org/sponsored/2024/06/generative-ai-for-security-harnessing-amazon-bedrock-for-customer-impact)

*03:30 PM, Monday, June 10, 2024*

By Martin Holste and Mark Weiss

Cybercriminals have more powerful tools than ever to compromise environments and threaten businesses. They use generative AI (GenAI) to install ransomware faster; deep-fake social engineering; cheap yet advanced spear-phishing attacks; sophisticated coding abilities; and even turnkey ransomware underground storefronts.

Such a range of AI-aided weaponry can leave security operations staff feeling hopeless. Often underfunded and understaffed, security teams must defend against all attacks from all routes, at all times. They need to investigate every alert, no matter how seemingly minor, as a threat. Keeping up means fighting fire with fire: employing GenAI to move quickly and scale a small staff for a big challenge.

To investigate every alert, companies can now use GenAI-powered tools to automate the investigation process by asking the right questions and producing sub-second data retrieval times for the answers. The potential to augment security with GenAI is high: a recent study from Trellix finds 91% of CISOs expressing excitement over the prospects and opportunities GenAI and AI will bring to their organization.

The first step to fighting GenAI cybercrime with GenAI security is to create a defensible environment: an instrumented infrastructure allowing visibility into all critical areas to see significant threats like ransomware.

Building this environment involves three lines of defense: detection, investigation, and response.

Detection and prevention tools alert security teams to attacks or breaches including endpoint protection, network detection, anti-phishing, and event anomaly detection.

Such security controls may stop an attack before it happens, but a motivated or lucky threat actor may bypass such initial preventive measures. So, using a wide range of security tools that cover as many routes as possible into an environment is critical.

At a minimum, defenders must be able to block malicious files, URLs, and emails. These protections often prevent 99% of attacks. But the other 1% remains a huge problem.

After the triggering event, defenders need the right context to prove what has happened. But it can be hard to know in advance what will be valuable in scoping a security incident.

Defenders need as much data from as many sources as possible, including:

• User authentication audit records

• Account permission change audit records

• Network connections

• Proxy and URL records

• Business critical application telemetry

• Cloud infrastructure audit logs

• Directory and personnel information

• Security alerts from all available tools

Having access to this information is not enough. This data needs to be centralized and indexed so it’s intelligible to detection tools and immediately and programmatically available. Preparing this data infrastructure can be daunting, but it’s critical to creating a defensible environment.

Detection needs to lead to action—remediation—to prevent the spread of ransomware. This means programmatically changing the environment to quarantine, seal off, or otherwise contain a threat actor through network firewall policy, endpoint containment actions, login disabling, or identity and access permission changes.

Automating Investigations with Generative AI

To move at the speed of ransomware, detection, investigation, and response must be automated with GenAI powering the bulk of the investigation workload.

How can defenders use this powerful technology to tie these strategic defense components together?

The answer is in using pre-built scaffolding of investigations to ensure that GenAI is grounded in its investigation, with a predefined list of vital questions to ask after experiencing a given security alert.

The answers these questions yield will only be as good as the questions themselves. That’s why it’s so important to have a comprehensive array of security telemetry that can quickly and accurately provide the necessary context for the AI-driven investigation. Without these questions and answers, the AI has little more to investigate than the original alert.

Suppose a security information and event management (SIEM) creates an alert for a brute-force attack from an identifiable IP address against an application’s login system:

ALERT: BRUTE FORCE ATTACK AGAINST 192.168.0.1 DETECTED

A standard SIEM might identify a login after the brute-force attempt and raise an alarm. But an AI-driven investigation can go further, acting tactically as a virtual junior analyst that asks questions of the environment based on billions of events:

• What level of access does this user have?

• How often does this user access this environment?

• Were any additional suspicious accounts created during this time?

• Was this user out of the office at the time of the attack?

Even more impressively, this “AI junior analyst” can make inferences as a human would. It can understand that the hostname “prod-iowa-dc” is likely a production domain controller in Iowa and can use this information to consider other data: login patterns, which URLs were accessed, or any other alerts from other security tools.

Using AI for Customer Impact

Cyberuptive, a cybersecurity consulting firm, wanted to scale its Managed Security Service Provider (MSSP) program to acquire more customers using the same number of staff. To do that, it needed to expand its existing human-scaled security program to be more efficient with its threat detection and response.

Recognizing the need for advanced automation in investigations, Cyberuptive sought to streamline the process and achieve quicker and more effective responses to emerging threats.

By using GenAI from Trellix Wise—hyper automation delivered across the Trellix XDR Platform and built on Amazon Bedrock—in the investigation process, the firm reduced response times, increased incident resolution efficiency, and enhanced overall security posture. GenAI empowered Cyberuptive to deliver superior support, efficient response times, and cutting-edge threat intelligence to its customers, setting apart in a competitive market.

Armed with a staff scaled by GenAI to investigate every alert, organizations’ defenders can catch threat actors with the same sophistication—and avoid becoming a victim of cybercrime.

Martin Holste is Field CTO, Cloud & AI at Trellix.

Mark Weiss is Strategic Initiatives Lead, DevSecOps at Amazon Web Services.

To learn more, please register to attend the webinar Gen AI for Security: Adoption strategies with Amazon Bedrock.

Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon through a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI.

