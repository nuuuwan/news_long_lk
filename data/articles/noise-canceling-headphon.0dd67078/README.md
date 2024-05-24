# Noise-canceling headphones use AI to let a single voice through

## Summary 🤖

A prototype artificial intelligence (AI) system named Target Speech Hearing allows noise-cancelling headphone users to select a specific person's voice to remain audible while all other sounds are cancelled out. Although currently a proof of concept, the creators are already in discussions to incorporate the technology into popular brands of noise-cancelling earbuds and hearing aids. By utilising an AI compression technique called knowledge distillation, this system allows AI models to work in real time in headphones with limited computing power and battery life. The software trains a smaller model to imitate the performance of a larger model, separating specific voices from the surrounding noise.


## Follow-up Questions 🤖

1. How precisely does the Target Speech Hearing system recognize and separate chosen voices from the surrounding noise?
2. Can the technology handle multiple languages or is it currently limited to English? 
3. How might the AI compression technique called knowledge distillation impact the effectiveness and efficiency of the system?
4. How successful has the system been in tests, particularly in noisier environments?
5. While the technology is a proof of concept, is there a timeline for when it might become widely available? 
6. Could Target Speech Hearing technology be misused, such as for eavesdropping or privacy invasion?
7. Can the system handle voices that change, such as due to a cold or aging?
8. Would this technology be beneficial for people with hearing impairments or other auditory disorders? Can it be calibrated according to individual needs? 
9. How do "teacher" and "student" models work together to imitate behavior and performance?
10. What are some potential applications, especially in the workplace or public spaces, for this technology? 
11. How can the system be improved to enroll a targeted speaker even when their voice isn't the loudest in the environment? 
12. Are there any concerns about the system draining battery life or requiring significant computing power, and how are these being addressed?

## Full Text

[https://www.technologyreview.com/2024/05/23/1092832/noise-canceling-headphones-use-ai-to-let-a-single-voice-through/](https://www.technologyreview.com/2024/05/23/1092832/noise-canceling-headphones-use-ai-to-let-a-single-voice-through/)

*11:55 AM, Thursday, May 23, 2024*

Modern life is noisy. If you don’t like it, noise-canceling headphones can reduce the sounds in your environment. But they muffle sounds indiscriminately, so you can easily end up missing something you actually want to hear. A new prototype AI system for such headphones aims to solve this. Called Target Speech Hearing, the system gives users the ability to select a person whose voice will remain audible even when all other sounds are canceled out.  Although the technology is currently a proof of concept, its creators say they are in talks to embed it in popular brands of noise-canceling earbuds and are also working to make it available for hearing aids. “Listening to specific people is such a fundamental aspect of how we communicate and how we interact in the world with other humans,” says Shyam Gollakota, a professor at the University of Washington, who worked on the project. “But it can get really challenging, even if you don’t have any hearing loss issues, to focus on specific people when it comes to noisy situations.”

The same researchers previously managed to train a neural network to recognize and filter out certain sounds, such as babies crying, birds tweeting, or alarms ringing. But separating out human voices is a tougher challenge, requiring much more complex neural networks. Related StoryNoise-canceling headphones could let you pick and choose the sounds you want to hearA neural network can recognize and filter out certain sounds, changing the way we choose to experience the world around us.

That complexity is a problem when AI models need to work in real time in a pair of headphones with limited computing power and battery life. To meet such constraints, the neural networks needed to be small and energy efficient. So the team used an AI compression technique called knowledge distillation. This meant taking a huge AI model that had been trained on millions of voices (the “teacher”) and having it train a much smaller model (the “student”) to imitate its behavior and performance to the same standard.

The student was then taught to extract the vocal patterns of specific voices from the surrounding noise captured by microphones attached to a pair of commercially available noise-canceling headphones. To activate the Target Speech Hearing system, the wearer holds down a button on the headphones for several seconds while facing the person to be focused on. During this “enrollment” process, the system captures an audio sample from both headphones and uses this recording to extract the speaker’s vocal characteristics, even when there are other speakers and noises in the vicinity. These characteristics are fed into a second neural network running on a microcontroller computer connected to the headphones via USB cable. This network runs continuously, keeping the chosen voice separate from those of other people and playing it back to the listener. Once the system has locked onto a speaker, it keeps prioritizing that person’s voice, even if the wearer turns away. The more training data the system gains by focusing on a speaker’s voice, the better its ability to isolate it becomes.  For now, the system is only able to successfully enroll a targeted speaker whose voice is the only loud one present, but the team aims to make it work even when the loudest voice in a particular direction is not the target speaker. Singling out a single voice in a loud environment is very tough, says Sefik Emre Eskimez, a senior researcher at Microsoft who works on speech and AI, but who did not work on the research. “I know that companies want to do this,” he says. “If they can achieve it, it opens up lots of applications, particularly in a meeting scenario.” While speech separation research tends to be more theoretical than practical, this work has clear real-world applications, says Samuele Cornell, a researcher at Carnegie Mellon University’s Language Technologies Institute, who did not work on the research. “I think it’s a step in the right direction,” Cornell says. “It’s a breath of fresh air.” hide

