# Research: How Top Reviewers Skew Online Ratings

[https://hbr.org/2025/01/research-how-top-reviewers-skew-online-ratings](https://hbr.org/2025/01/research-how-top-reviewers-skew-online-ratings)

*01:15 PM, Thursday, January 09, 2025*

Yagi Studio/Getty Images

Online platforms from Amazon to Goodreads to IMDb tap into the so-called “wisdom of the crowd” to rate products and experiences. But recent research suggests that more experienced buyers tend to select better products and therefore expect higher quality,...more

Today, consumers often begin a new TV series by confirming its “fresh” status on Rotten Tomatoes, book a restaurant based on its Yelp ratings, and consult product reviews before making a purchase on Amazon.

But how much can we trust the information in these reviews? Beyond the well-documented issue of fake reviews, simply aggregating raw ratings may be misleading. As we documented in our research, forthcoming in Management Science, this is due to a combination of two factors: More experienced consumers tend to both purchase — and rate — higher-quality products and, as a result, to have higher expectations. The result? Higher-quality products are held to a higher standard and may receive lower average ratings than their lower-quality alternatives.

Examples of this bias are easy to find. A professional-grade camera may seem underwhelming to the National Geographic photographers who purchase it, as they’re accustomed to top-tier equipment. In contrast, a lower-quality camera might delight amateur users. The same distortion applies when comparing Michelin-starred restaurants with fast food chains, business class with economy flights, or five-star hotels with budget motels. Because the consumers for these goods come from distinct segments, comparing their ratings results in an “apples and oranges” dilemma, misleading future buyers.

One could argue that pricing explains these differences — shouldn’t a Michelin-star restaurant costing hundreds of dollars be held to a different standard than a $10 fast-food meal? While this is undoubtedly a valid point, we thought it was only half of the story. To prove it, we chose to study this bias in a market with uniform pricing: movies.

The Case of Movie Ratings

We analyzed more than 9,000 movies on IMDb that received a total of more than 650 million ratings. IMDb conveniently highlights the average score for each movie and provides separate scores from its “Top 1,000” users — those who have rated the most titles on the platform. To deepen our analysis, we also incorporated 15 million individual ratings from MovieLens, a popular movie recommendation site. To measure quality, we used external proxies such as festival awards, nominations, and reviews from professional critics.

As expected, the Top 1,000 users on IMDb tend to watch higher-quality movies and rate them more strictly. Among movies with similar characteristics — year of production, genre, and number of reviews — those with at least one award or nomination received more than 5% more ratings from Top 1,000 users. What’s more, these users gave lower scores than the average user for an astonishing 98% of the movies we studied.

Together, these findings reveal a clear bias against higher-quality movies: Because these films must impress a more knowledgeable and critical audience, their ratings suffer relative to their lower-quality counterparts.

An Easy-to-Implement Remedy

This bias, while pervasive, can be corrected with a straightforward solution. The key is to adjust for users’ stringency when calculating ratings. Based on individuals’ ratings from MovieLens, we measured each user’s “strictness” by comparing their ratings to the average score for the same movies. For instance, if a user consistently rated movies lower than others, we inflated their ratings accordingly. We then recalculated adjusted ratings for each user and aggregated them for each movie. Since ratings and strictness are interdependent, we repeated this process until the adjustments stabilized.

The results validated our theory: The adjusted ratings better correlated with external quality proxies, such as nominations and awards from major film festivals like Sundance, Toronto, Cannes, and Venice.

Implications for Platforms

Our study highlights a core problem with consumer ratings. Even if we were to assume that every consumer rates honestly (but subjectively) and that no fake reviews are present, comparisons of average scores can be deeply misleading about products’ relative qualities, since different products are held to completely different standards.

Our results also offer a potential explanation for the longstanding divide between the opinions of critics and everyday consumers. While taste may play a role, our findings suggest that this divide is also fueled by the flawed aggregation of consumer opinions. Looking at the ratings of average and Top 1000 users (the latter could, in many ways, resemble professional critics in their taste and rating behavior) further validates this point, as we find a very high correlation between the two. In other words, average and Top 1000 users tend to like the same movies, but Top 1000 users tend to like virtually every movie less.

Several platforms prioritize and amplify reviews from their most experienced users. While this strategy has its obvious merits, it can inadvertently further penalize higher-quality products by overemphasizing stricter reviews. To address this, platforms could normalize ratings by adjusting for user stringency. This approach also offers additional benefits: for instance, it discounts suspiciously glowing ratings from fake or paid reviewers without requiring explicit identification of fake reviews.

Managers should also rethink their reliance on early reviews from highly experienced consumers. While these users often provide detailed and thoughtful feedback, their stricter standards can result in harsher evaluations. For example, authors soliciting early reviews on Goodreads might find that top reviewers rate their books more critically than general readers.

Ultimately, platforms must recognize that biases in consumer ratings are not just a consequence of bad actors (e.g., fake reviews) but are deeply embedded in the design of feedback systems. Algorithms that adjust for this bias offer a promising path forward, enabling marketplaces and networks to enhance the fairness and reliability of their products.

Readers Also Viewed These Items

Employment Is Dead: How Disruptive Technologies Are Revolutionizing the Way We Work

The Secrets of Great Culture (HBR Special Issue)

Read more on Consumer behavior

