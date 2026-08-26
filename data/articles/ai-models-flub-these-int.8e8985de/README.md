# AI models flub these intelligence tests. Can you fare any better?

[https://www.technologyreview.com/2026/08/26/1141952/puzzles-ai-models-flub-these-tests/](https://www.technologyreview.com/2026/08/26/1141952/puzzles-ai-models-flub-these-tests/)

*05:00 AM, Wednesday, August 26, 2026*

Puzzles and games have been central to AI development since the very beginning. Just as we humans like to test our smarts with crosswords or logic puzzles, developers can test how far models have advanced with a gaming gauntlet. The term “machine learning” was popularized in a 1959 article by the IBM computer scientist Arthur Samuel about an algorithm that learned to play checkers. Chess and the Chinese board game Go are famous AI test beds too.  Judged purely on its puzzling skills, AI is improving a lot—and quickly. In late 2024, a team of scientists from Columbia University showed that even the best models could figure out only 18% of the infamous New York Times Connections puzzles; by early 2025, some models could solve them near perfectly every time.   But puzzles do more than just highlight the inexorable advance of AI capabilities. Seeing where models succeed and fail—and where we humans still beat them—can provide a useful window into the technology’s strengths and weaknesses. Despite advances, today’s models still fumble: Subtle changes in classic riddles often trip them up, and visual puzzles are a particular weak spot.  Here you’ll have the chance to test your wits on puzzles that have stumped models at one time or another. Some might be as tricky for you as they were for the AI; others are so simple that they’ll have you doubting whether AI is really intelligent at all. Each one highlights at least one way in which machine and human cognition differ. If you ace the test, you’ll have proved that you can out-puzzle an AI—at least for now.  Advertisement  Spatial Reasoning Let’s start with a domain where humans have a huge advantage: spatial reasoning. If you’ve ever taken an IQ test, you may have done a mental rotation problem. These puzzles ask you to determine whether different images represent the same objects from different angles. Though today’s language models typically have the ability to analyze visual inputs, they still fail abysmally at these puzzles. For all the talk of how world models can help AI understand physical environments, LLMs still don’t seem to be able to manipulate 3D objects the way spatial thinkers like architects and mechanical engineers can. Mental Rotation Instructions: Choose the answer that shows the object in the prompt, but from a different angle. In each case, there’s only one correct answer!

Memory & Adaptability Frontier LLMs have extraordinary memories; they were exposed to a monstrous volume of facts during training and can recite many of them faithfully. That’s an asset for outcompeting humans at trivia, but it can also be a liability. When a puzzle closely resembles one a model saw during training, the model may whiz by key differences and respond with what it memorized.  This held true in a 2024 study in which researchers from Google and the University of Illinois Urbana-Champaign trained and tested models on slight variations of a classic type of puzzle called Knights and Knaves. In these problems, some characters always tell the truth and others always lie, and you have to figure out who’s who. The same principle may be at work in a test called SimpleBench. These questions resemble more complicated problems that models likely encountered in training. Humans spot the trick, but even top-tier models trip.

Knights and Knaves Instructions: The only thing you need to know to solve these puzzles is that knights always tell the truth and knaves always lie. Determine who’s what on the basis of what each character says.

You have met a group of two islanders.

Their names are Edward and Wallace.

Edward tells the truth.

Wallace and I are the same type.

You have met a group of three islanders.

Their names are Joseph, Francine, and Alice.

Alice tells the truth.

Joseph is not my type.

You have met a group of three islanders.

Their names are Robert, Vincent, and Michelle.

Michelle is truthful.

Vincent is untruthful.

Vincent is not my type.

SimpleBench Instructions: Read these SimpleBench problems carefully, and you should be able to figure out the answers in no time.

frying pan at the start of the

first minute, then five at the

start of the second minute

and some more at the start

of the third minute, but none

in the fourth minute. If the

average number of ice cubes

per minute placed in the pan

while it was frying a crispy

egg was five, how many

whole ice cubes can be

found in the pan at the end

solid blue ball a meter

in the air and then a solid

purple ball (of the same size)

two meters in the air. She

then climbs to the top of a

tall ladder carefully, balancing a yellow balloon on her

head. Where is the purple

ball most likely now, in relation to the blue ball?

At the same height as the blue ball

At the same height as the yellow balloon

Above the yellow balloon

Abstract & Visual Reasoning AI doesn’t just bungle visual problems in 3D—two dimensions can trip it up as well. That’s a major factor in how well models do on the most famous ­puzzle-based benchmark, ARC-AGI. These problems require you to infer abstract, general rules from a set of examples. Models do better on ARC puzzles when they receive each grid not as an image but as a string of numbers that encodes the color of each cell.  Research suggests that even when models answer ARC-AGI questions correctly, they often do so using byzantine and non-­generalizable rules, whereas humans draw on simple visual concepts. Despite these disadvantages, models have gotten quite good at ARC-AGI over the past year, but some puzzles—such as the one printed here—still stump them. ARC-AGI Instructions: Study the three pairs of grids shown below to figure out the rule that dictates how the ones on the left transform into the ones on the right. Then get out your markers or colored pencils and fill in the fourth grid using that rule. (The solution is the same no matter which way the grids are oriented.)

Check answerReveal solution

Intuition It’s not just AI models that fall into traps. We humans have our own cognitive foibles, many of which AI does not share. Psychologists have designed problem suites that invert the SimpleBench phenomenon: For these questions, humans often give knee-jerk answers, whereas models will respond deliberatively. Some of the problems exploit errors in the ways that we intuitively do math; others are phrased so as to suggest obvious answers that fall apart if the question is read carefully.

Advertisement Lightning Round Instructions: Answer the questions below as quickly as you can.

In a cave, there is a colony of bats whose population doubles each day. Given that it takes 60 days for the entire cave to be filled with bats, how many days would it take for the cave to be half-filled with bats?

In what famous novel does Alice state "I'm late, I'm late, for a very important date"?

Increasing Complexity In some cases, whether an LLM can complete a puzzle is a matter of scale. One study from researchers at Apple found that LLMs can ace simple versions of the Tower of Hanoi problem, which involves moving a stack of disks one at a time without ever putting a larger disk atop a smaller one, and river-crossing puzzles, in which a group of people must traverse a river according to certain rules. But only up to a point: As the number of disks or people hits six and higher, the models began to falter.  In another study, researchers at the University of Washington, Stanford University, and the Allen Institute for AI observed that LLMs struggle similarly with logic grid puzzles, which require deducing the attributes of a set of individuals from a list of clues. The Apple paper went viral, but commentators questioned whether the results reveal a unique limitation of LLM reasoning—or just that it’s normal to make errors as complexity piles up. The River Instructions: Using the scenario provided, plan the trips necessary to get everyone across the river.

Three FBI agents and their three informants need to cross a river. They have a rowboat that can fit only two people, though it can be rowed by only one. Each agent will refuse to leave their informant on the same bank as other agents without them present—even if the informant never steps out of the boat and onto the bank. How can all six make it across?

Logic Grid Instructions: Using the list of clues, determine who lives in each house and what style of music each person enjoys. There is only one possible solution. You may find it helpful to fill out the grid below to keep track of your deductions.

There are 4 houses, numbered 1 to 4 from left to right, as seen from across the street.

Each house is occupied by a different person: Peter, Eric, Arnold, or Alice.

Each resident has a favorite type of music: jazz, rock, classical, or pop.

Alice is directly left of Peter.

The person who loves classical music is directly left of Peter.

Arnold loves jazz music.

The person who loves rock music is not in the second house.

The person who loves rock music is directly left of the person who loves pop music.

Click a cell to mark an X, click again for a check mark.

House1234MusicJazzRockClassicalPopResidentPeterEricArnoldAliceMusicJazzRockClassicalPop

Check answerReveal solution

Grace Huckins is an AI reporter at MIT Technology Review. They have a PhD in neuroscience.  Credits:  Mental Rotation: CC BY 4.0. Stogiannidis, Ilias, Steven McDonagh, Sotirios A. Tsaftaris. Mind the Gap: Benchmarking Spatial Reasoning in Vision-Language Models (copyright 2025); illustrations by John MacNeill. Knights & knaves: Courtesy Dan MacKinnon. Simplebench: CC BY 4.0. SimpleBench Team. The Text Benchmark in which Unspecialized Human Performance Exceeds that of Current Frontier Models (copyright 2024). ARC-AGI: Courtesy ARC Prize Foundation. Lightning round: CC BY 4.0. Hagendorff, Thilo, Sarah Fabi, Michal Kosinski. Human-like intuitive behavior and reasoning biases emerged in large language models but disappeared in ChatGPT. Nat Comput Sci 3, 833–838 (copyright 2023). The river: Adapted from Propositiones ad Acuendos Juvenes, Alcuin of York (ca. 800 CE). Logic grid: Apache License 2.0. Lin, Bill Y., Ronan Le Bras, Kyle Richardson, et al. ZebraLogic: On the Scaling Limits of LLMs for Logical Reasoning (copyright 2025)

