# How Companies Can Use LLM-Powered Search to Create Value

[https://hbr.org/2024/10/how-companies-can-use-llm-powered-search-to-create-value](https://hbr.org/2024/10/how-companies-can-use-llm-powered-search-to-create-value)

*12:15 PM, Friday, October 11, 2024*

Soon, searching through links may be replaced by conversational interfaces that will allow users to refine queries and deepen their understanding through follow-up questions — and audio, video, and images are all part of this new search and retrieval paradigm. Consider...more

As large language models (LLM) continue to advance at a dizzying pace, many business leaders are still grappling with how to put this technology to work. On one hand, they’re looking for areas where these generative AI tools can quickly prove their value. On the other, they want to lay a foundation for broader-scale and long-term transformation.

AI is becoming a natural part of everything we do and intrinsic to every facet of business, seamlessly integrating into various processes to enhance efficiency and innovation. One promising area that can deliver both immediate impact and help lay the groundwork: LLM-powered search and retrieval. It’s an approach that can fundamentally change how companies interact with their own data to unlock insights, spark new ideas, and inform better decision-making.

Web browsers have already adopted this capability, using it to enhance search with AI-generated summaries and overviews. Soon, searching through links may be replaced by conversational interfaces that will allow users to refine queries and deepen their understanding through follow-up questions. And they’re not limited to text — audio, video, and images are all part of this new search and retrieval paradigm. This multi-modal experience is only one reason why users continue to gravitate to more advanced applications of AI-enabled search.

Now, consider how those powerful capabilities might translate across your business: chat-based tools that allow employees to easily query policy documents, conduct quick Q&As with the organization’s latest sales data, or have meaningful conversations with all manner of institutional knowledge. And there are even larger opportunities. These advanced gen AI search and retrieval capabilities can assist in document generation, report generation, code generation, recommendation systems, and much more.

In this article, we will explore the latest techniques powering gen AI-based search and retrieval and share innovative, real-world use cases that are delivering payback today. We will then discuss the risks & challenges associated with these use cases — and share six tactics businesses can deploy to leverage this capability effectively and responsibly.

LLM-Based Search has Become More Powerful

Over the last few years, LLMs have evolved rapidly, but so have the broader software environments they are part of. Specifically, many LLMs have been enhanced by an innovation called “retrieval augmented generation” (RAG), where content is served from a known fact base, which helps make retrieval more reliable and lessen the cost burden on fine-tuning (or retraining) of the LLM. The use of RAG and other recent technical innovations are a direct response to earlier challenges, notably with hallucinations or other erroneous responses the systems may have returned. The RAG ecosystem is rapidly improving the accuracy of retrieval as well as content generation using that retrieved content. These improvements allow businesses to leverage their own unique data sets, transforming business processes and ways of working by tying an inquiry to a set of known documents.

RAG systems are also being used with “reinforcement learning with human feedback” (RLHF), which refers to combining retrieved knowledge with human feedback to refine the model’s behavior and generate more accurate, contextually relevant responses. This allows users to guide the system to prefer certain content within the search or vector index based on individual user feedback and prioritize content they perceive as more relevant to their use case. This has applicability across multiple domains. For example, an HR portal using RAG with RLHF could enable the system to prioritize and surface HR policy information that aligns with an employee’s specific needs or recurring queries. Over time, the system would learn and adapt to prefer documents and guidelines that the employee frequently references or finds particularly useful, thereby creating a more tailored and efficient information retrieval process.

These improvements unlock new potential for both humans and LLM-backed agents, which are designed to perform microtasks and work in concert with one another to achieve a larger goal with human input to help drive the process. And now, a growing number of companies are aiming to address pain points in the data workflow, from the database structures themselves to how to improve the data pipelines.

Getting better information faster is always a business priority. On public search engines, AI-generated summaries have changed users’ starting point: Instead of clicking through links and trying to orient themselves, they can scan an answer collated from the top search results. It probably isn’t going to be perfect, but it helps orient their research. This is the experience that businesses are looking to embed into their own systems. Surfacing answers to relevant queries ranging from internal questions like those related to enterprise policy but also external-facing agentic systems that are intended to interact with customers.

We are already seeing real examples of this across industries. For instance, one company has improved how it responds to customer issues and the efficiency and effectiveness of its call center operations. By using RAG to “embed” the LLM with its internal knowledge bases, a combination of human- and gen AI-based customer service agents quickly zero in on the information that’s relevant to the customer and provide more tailored results tied to real, credible company-specific information. RLHF further refines this process.

Or look at IT, where similar approaches are being used to improve the software development lifecycle (SDLC). With access to business requirements, product documentation, and code repositories, the LLM and agent systems are automating and improving the quality of backlog curation, test case generation, code generation, and other key SDLC areas. While these may not seem like use cases directly related to idea of search and retrieval, at the core they adhere to the same core requirements: processing a query to understand its core intention, mapping to relevant existing information, and retrieving known content that can serve the inquiry effectively.

Agentic LLM solutions and other GenAI-enabled search systems are not without potential faults; no technology solution is. While RAG and other innovations enable access to better, more relevant data, they don’t eliminate the risk of hallucination, for instance. Gen AI systems can — and do — still surface poor information. Take for instance if a system is designed to retrieve policies relevant to a query. What happens if there are multiple versions of the same type of policy in the repository? Or what if there is conflicting guidance across several different policies?

Companies need to be able to articulate how erroneous responses may surface and build awareness amongst users and developers alike.

This project should fall under a responsible AI framework that provides an enterprise-wide approach to identifying, mitigating and monitoring the various risks associated with the use of AI is needed to remediate these issues. For example, developing a shared understanding of what is believed to be an authoritative data source is necessary; the models themselves do not have awareness to know this, they should be instructed, or misinformation may spread. The old adage of garbage in and garbage out still applies in this domain of gen AI. So taking the time upfront in the process to have well curated data will benefit you in the long run in terms of accuracy and consistency.

Another risk of gen AI systems has been data leakage and other privacy issues, and RAG-type implementations don’t fully rectify these either. Over the past year and a half, a major push by enterprise users was to have a secure instance of gen AI models deployed on their premises, with none of their data (prompts, documents, etc.) flowing back to the vendor or open-source community. However, these local deployments don’t prevent some leakage across the organization — a person in sales might gain access to sensitive HR data if it is exposed to the same model. For this reason, we continue to advocate for governance practices that require firewalls where sensitive data is considered and should be safeguarded.

Then there are risks such as bias and transparency, which persist because these issues stem from multiple sources: the underlying gen AI model, the intended use of the application, and the expectations of the users. While vendors themselves have been pushing to improve asynchronous monitoring capabilities to responsibly identify potential harmful information being produced, enterprises themselves still need practices in place to enable effective use for search and retrieval. Being aware of what a biased retrieval may look like and incorporating additional instruction for its mitigation in the context of specific use — especially when sensitive information, including that about people or communities is incorporated — is an enterprise capability that needs to be developed as part of a broader responsible AI framework.

And while internal enterprise use may have limited cybersecurity challenges relative to applications with external consumers, enterprises still need to remain vigilant regarding potential attack vectors such as data and prompt poisoning, which may derail effectiveness of solutions over time for a wide range of users. Monitoring is still required for each use case and application to understand how it is being used or misused, and where performance may decay.

Six Tactics to Leverage this Capability Effectively — and Responsibly

While challenges persist and may continue to evolve over time, there is no doubt that the shift to LLM and gen AI-enabled search and retrieval will continue. To do so effectively, organizations should consider following several steps:

1. Clearly define use cases.

Collaborate between the business teams defining the requirements and the technical teams or vendors responsible for building and deploying to align on a solution with clearly measurable outcomes to enable evaluation down the line

2. Establish intake processes that consider risk as well as value.

Consider not just the ROI of the use case, but also sensitivity of the data being used, the potential for harm with the application overall, and the intended users when prioritizing which use cases to invest in. Incorporate a risk-tiered approach to evaluating use cases

3. Invest in practices surrounding data collection, testing and validation so you have effective ground truth.

Recognize that effective use of LLMs, especially those used in search and retrieval tasks, still need a solid fact-base to work from. Data transformation efforts therefore should continue, and keeping a focus on both the quality of data feeding the models as well as the overall workflows to source, label, store, access, and process data are key

4. Incorporate standardized testing practices.

Ad hoc evaluation will only go so far; align on a standard model development process supported by playbooks and pre-defined testing practices to enable quality, resilient, and well tested systems

5. Establish monitoring capabilities.

Appreciate that things change — data changes, how users interact with systems will change, technology changes, and what may be needed from systems change over time. Recognize that these systems need to be monitored for ongoing performance, and metrics need to be determined so there is something (and some way) to monitor.

6. Roll out training, awareness and communication campaigns.

Equipping your employees with the knowledge to effectively and responsibly build, deploy and leverage gen AI tools is as important as the technical infrastructure and risk management controls that need to be put in place. Identify the gen AI-related learning and awareness needs throughout your organization and launch tailored education and communication programs

Search is likely to remain a dominant application for large language models and multimodal GenAI for some time to come. But these systems still require effective data, tooling, and governance to operate effectively, at scale. Responsible AI and associated governance practices should underpin all deployment of AI. With a technology landscape shifting as quickly as it is, consider use cases based on impact and risk, and invest in underlying functions that enable you to scale responsibly across a multitude of areas.

Readers Also Viewed These Items

Leading Through: Activating the Soul, Heart, and Mind of Leadership

HBR Guide to Leading Through Change Toolkit

Read more on Generative AI

Technology and analytics,

AI and machine learning,

Business law and ethics
