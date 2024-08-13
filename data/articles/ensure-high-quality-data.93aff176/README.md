# Ensure High-Quality Data Powers Your AI

[https://hbr.org/2024/08/ensure-high-quality-data-powers-your-ai](https://hbr.org/2024/08/ensure-high-quality-data-powers-your-ai)

*12:15 PM, Monday, August 12, 2024*

AI does not need to fail on a global scale to cause enormous damage — to individuals, companies, and societies. Models frequently get things wrong, hallucinate, drift, and can collapse. Good AI comes from good data, but data quality is an enormous...more

Twenty years ago, mortgage-backed securities and collateralized debt obligations were all the rage. These new financial products were, initially, a wonder: they helped put millions of people into homes and make billions for banks. Then things went horribly wrong, and they nearly tanked the global economy.

The financial crisis of 2007–2009 has been studied from many perspectives, but viewed through a data science lens, it provides two insights that serve as a cautionary tale for artificial intelligence and machine learning (which I’ll simply refer to as AI) today:

First, the analytical work to slice and dice mortgages into products that fit investors’ different risk-reward profiles was actually quite good. But results depended on the data being high quality.

Second, the data was not, in fact, high quality. Bad or missing data appeared at every step, from incorrect (sometimes fraudulent) information on mortgage applications to incorrect credit scores and securities ratings, lost paperwork, and a lack of clarity in bank liabilities. The subpar data led banks to vastly under-estimate risks, leading to an unexpected number of foreclosures, in turn causing banks to not trust each other’s liability statements, and the banking system to freeze up.

The lesson at the heart of this story is a simple one: good data science + bad data = bad business results.

What does this have to do with AI? For one, the hype surrounding AI is far greater and more pervasive than was the hype around financial products. Worse:

The math used to slice and dice mortgages was well understood. In contrast, even experts aren’t sure why AI makes the predictions it makes.

The quality requirements for AI are far broader and deeper.

While the analytics work for financial products was performed by professionals who understood, or should have understood, the importance of quality data, better tools make AI accessible to people who less informed on all that can go wrong.

AI does not need to fail on a global scale to cause enormous damage — to individuals, companies, and societies. Models frequently get things wrong, hallucinate, drift, and can collapse. Everyone has their favorite, “look at this ridiculous answer a large language model gave me” or “AI disaster story.” Coupled with the high failure rate of AI projects, it is not hard to see why few companies can cite a positive ROI.

Warnings about data quality have been plentiful, coming from sources as diverse as those leading the AI revolution, including Google, Meta, Open AI; prominent researchers; and the popular press including the New York Times, and the Economist. Forrester, the research firm, advises that “Data Quality Is Now the Primary Factor Limiting Gen AI Adoption.” Yet most companies have not even started the work they need to do.

The primary interest here is a company’s first several AI projects. Importantly, data quality is an enormous organization-wide issue (and opportunity), yet most companies have neglected it. One consequence is that they, and their senior leaders, don’t understand the issues, how to address them, and the organizational changes they must make. They are in a tough spot — they must protect themselves in the short-term, build needed longer-term capabilities, and simultaneously educate themselves so they can do so effectively. This article aims to help them get started.

Understanding the problem

Any data science project should start with level-headed thinking about the problem one wishes to solve. To illustrate, consider, “We need a better way to decide which loans to grant and under what terms?” Clearly stating the problem involves asking and answering questions, such as “better how?” and “which loans to whom (e.g., the population of interest)?”

The answers loom in determining what data you need. For examples:

If “better” means bias-free, you’ll need a bias-free training data, which may be very hard to come by.

If “better” means more “performing loans” and fewer “non-performing loans,” you need data on loans that you have not granted historically.

If “better” means decisions that can be more easily explained to regulators, AI may not be your best approach, for “explainability” is fiendishly difficult.

If “better” means “will work in parts of the world in which we don’t currently operate and don’t have data,” you have a tough challenge.

If “better” means a cheaper overall process, your historical data may be just fine.

Coming to agreement on the problem can be highly political. Those eager to bring AI into the organization may be motivated by completing a “use case” to prove AI works, while others may want to allay fears that competitors are roaring ahead, and still others may wish to get regulators off their backs. All such perspectives are valuable, and it is tempting to plow ahead before the problem is clearly stated. Doing so is ill-advised.

“Garbage in, garbage out” might be a useful rule of thumb, but I find it convenient to frame the idea of good data through two requirements: 1) whether it’s the “right data” to address the problem and 2) whether that “data is right,” or correct. The criteria for the latter are more familiar to most people: accuracy, absence of duplicates, and so forth. Having the “right data” is less familiar, more subtle and complex — but it’s also essential.

When sorting out the right data for a project, consider:

Relevance and completeness: AI depends on data with predictive power, that is data relevant to the problem at hand. For instance, attributes such as age, payment history, and income are clearly relevant to loan decisions. Completeness involves having as many relevant data attributes as possible.

Comprehensiveness and adequate representation: The two main issues are “does the data adequately cover the population of interest (comprehensiveness) and all subpopulations (adequate representation) of interest?” After all, it takes a lot of data to properly train a model. To illustrate adequate representation, note that if you wish your model to work world-wide, you’ll need data from all over the world.

Freedom from bias: Reducing historical bias is (or should be) important in most problems involving humans. Unfortunately, many data sets reflect historical biases and removing those biases from data sets may be near impossible. In such situations, companies should not use AI.

Timeliness: The essential issue is “how new must the data be?” In the loan example, making decisions quickly using the most up-to-date data may prove a source of competitive advantage.

Clear definition: Most AI efforts pull data together from disparate sources and a good understanding of those sources and the data they provide makes combining them easier. Clear definitions, of sources, data attributes, and measurement units, make developing this understanding easier.

Appropriate exclusions: Certain data should be excluded for legal, regulatory, ethical, and intellectual property considerations. For example, using zip codes can be a surrogate for race in loan decisions, and you must avoid violating laws stipulating how personally identifiable information (PII) may be used. Further, there is growing concern that AI models trained on public sources may violate intellectual property rights.

Most important data right considerations:

Accuracy: Accuracy is the probably the best-known feature of data quality. The essential idea is that data values must be “correct,” that is they must reflect reality. Though subtleties, such as “how closely must the data values represent reality?” are sometimes important, most structured data sets are riddled with errors. And it stands to reason that documents (unstructured data), which are used to train Large Language Models are in worse shape.

Absence of duplicates: It is easy for duplicate entries to slip into databases, and they can skew results. Thus, they must be kept to a minimum

Consistent identifiers: When pulling loan data together, is this “John Smith,” with a checking account, and that “J. E. Smith,” with a home equity line of credit, the same person. You have to know so you can integrate data together.

Correct labeling: Good data labels (e.g., “this is a cat,” “this loan is performing”) improve AI models.

The data-quality job does not end with training. Train a model well on high-quality data and you get a good model. But feed that model bad “future data” and you get bad results/ predictions. Both the “data is right” and “right data” criteria remain in force.

One woman was denied pain killers because prescriptions for her dog were ascribed to her (i.e., the data was wrong). This led a model to label her as at risk for opioid addiction. Similarly, feed a model data beyond the realm on which it was trained and there is no telling what will happen. This occurs rather frequently because conditions in the world have changed, leading data inputs from new domains, and, often, degraded model performance. Sometimes the deterioration is severe. Microsoft’s Tay chatbot, which started spitting hate speech when users fed it vile phrases, on which it was not trained, serves as a cautionary tale.

In the short-term, adopt a “guilty until proven innocent” stance.

The most important step in any data-quality project or program involves “getting the management responsibilities right.” And for any given AI project, it is tempting to assign quality to those closest to the work, including modelers, data engineers, and data wranglers. While all can do some good work in understanding sources and cleaning the data, they are not equipped to pull together the full range of effort required. To illustrate, “defining the problem” is a business issue, not a modeling, engineering, or wrangling issue.

At the project level, overall responsibility for data quality must reside with the highest-level person leading the effort. They must pull together teams of people who can develop the full suite of requirements and dive into details to ensure they are met. They should consider acquiring external talent, if as is often the case, their companies lack the breadth and depth of skill needed to do so.

These managers themselves should relentlessly question model development teams and others about everything. Start with “are the problem you set out to solve and our problem the same?” If not, be very careful. Next, work through the right training data criteria one at a time. Dig deep — what makes you think the data will yield good predictions, support extending the model to new markets, and is bias-free? Be wary when vendors decline to answer, citing “our model is proprietary.” The model may be proprietary, but that doesn’t mean the data is.

With respect to the “data right,” modelers almost certainly need to perform extensive cleanup of training data. Ask them to detail how they measured accuracy before and after clean-up, how they found and eliminated duplicates, how they ensured data integration, and how they ensured that labels were correct. Push very hard and, if you detect any softness in the answers, insist modelers obtain better answers.

Management responsibilities extend to future data. Managers must monitor future data aggressively to ensure it doesn’t stray too far from the bounds of the data on which it was trained. They must insist on in-depth controls to make sure that future data is as complete and accurate as is possible.

Finally, senior leaders and boards should also insist on quality assurance, in the form of independent review to make sure that all the issues called out here are understood, embraced, and acted on in an appropriate manner. Especially early on, a bit too much QA is better than too little.

In the mid-term, push quality efforts upstream.

Data scientists, like everyone else in a company, depend on others for data. Marketing creates data used by Sales; Sales creates data used by Operations, those building AI models use data created by many sources and, in turn create data in the form of predictions. Today each group spends an inordinate amount of time dealing with bad data: perhaps 30% across the company and 80% in data science.

Fortunately, there is a better way: Eliminate root causes of bad data upstream and those downstream don’t have to deal with them! This approach builds on what worked in manufacturing and has proven itself time and again at companies such as AT&T, Gulf Bank, Chevron, and others. As a practical matter, this works best when downstream groups take on roles as data customers; upstream groups take on roles as data creators; and the two work together to sort through quality requirements, make some basic measurements, then find and eliminate root causes of error, one at a time.

Thus companies should transition from the dealing with bad data downstream to creating good data upstream. Like any other discipline, quality management provides a rich body of underlying foundations, methods, and tools on who does what. To bring them into your organization, start with three concepts:

Intense focus on customer and process improvement, with the long-term goal of creating the right data correctly with proper identifiers and labels, the first time.

Clear management accountabilities: Making clear that business departments, not IT, the Chief Risk Officer, or the Chief Data Officers, are responsible for data quality. In turn, this means clear roles responsibilities for teams and individuals.

Get as many people as you can, at all levels, as involved as you can.

Don’t get overwhelmed.

I know that some will react, “Oh my goodness, this is far too expensive.” But in point of fact, these recommendations save money. As noted, companies spend an inordinate amount their time on non-value-added data work. Following these recommendations cuts that cost dramatically.

The more pertinent reaction is “Oh my goodness, this will require real transformation.” That is true! If you’re not up for it, perhaps you should scale back your AI ambitions.

More pro-actively, companies are beginning to realize that, properly managed, data becomes an asset of potentially limitless potential. It deserves proper management. AI unlocks that potential. Simply stated: To get great results from high-quality AI, you need high-quality data.

Digital Intelligence  Course

Accelerate your career with Harvard ManageMentor®. HBR Learning’s online leadership training helps you hone your skills with courses like Digital Intelligence . Earn badges to share on LinkedIn and your resume. Access more than 40 courses trusted by Fortune 500 companies.

Excel in a world that's being continually transformed by technology.

Learn More & See All Courses

Readers Also Viewed These Items

Managing Conflict: Disagree Productively (Virtual Group Learning)

The Anxious Achiever: Turn Your Biggest Fears into Your Leadership Superpower

Read more on Analytics and data science

AI and machine learning

and Technology and analytics

