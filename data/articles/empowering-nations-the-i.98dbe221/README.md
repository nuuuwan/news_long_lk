# Empowering Nations:The India-Sri Lanka HVDC Connection

[https://www.dailymirror.lk/hard-talk/Empowering-NationsThe-India-Sri-Lanka-HVDC-Connection/334-291374](https://www.dailymirror.lk/hard-talk/Empowering-NationsThe-India-Sri-Lanka-HVDC-Connection/334-291374)

*03:13 AM, Tuesday, September 10, 2024*

Dr. Manilka Jayasooriya is a Sri Lankan-born engineer currently working at Staffordshire University as a Lecturer. He achieved his PhD in 2020 for a highly miniaturized novel RFID fractal antenna for a doorway reader document tracking application. He received his MSc degree in electronics with distinction at Staffordshire University. Dr. Jayasooriya has contributed to several industrial and government projects in sustainable energy innovation. One of his notable designs was at Bibliotheca Library Solutions where he designed a detachable electromagnetically coupled handheld RFID reader antenna for Marks and Spencer. His current research interests include power electronics, renewable energy integration and line protection of HVDC grids

Sri Lanka and India are engaged in a decade-long discussion of linking their power grids, which would be beneficial for either country as energy consumption in both nations is expected to grow in large proportions. The latest discussion or rather the fifth of the India – Sri Lanka Joint Working Group for cooperation in the power sector was held last February in Sri Lanka co-chaired by the Secretary to Indian Ministry of Power Pankaj Agarwal and the Secretary to the Ministry of Power and Energy Dr. Sulakshana Jayawardena.

Whilst the proposal to lay a direct transmission line between Anuradhapura and Chennai is expected to raise hopes of the country’s energy security, the Sri Lankan-born scientist from the UK Dr. Manilka Jayasooriya emphasizes the plan is not farfetched from reality.

What is the India-Sri Lanka HVDC link and why is it important for both countries?

The India-Sri Lanka HVDC link is a proposed high voltage direct current interconnection aimed to enhance energy security and promote sustainable development for both nations. It facilitates the exchange of electricity, optimising the use of renewable energy resources, reducing reliance on fossil fuels, and strengthening the regional power grid’s resilience. This project is crucial as it supports economic growth and environmental sustainability in the region. Notice over the past 50 years the global energy landscape has evolved rapidly driving increased grid integration across territories and nations, and there is a global movement towards an ‘ecological civilisation’. This is a concept proposed by China followed by Europe and Africa which emphasises sustainable development and harmonious coexistence with nature.

Dr. Manilka Jayasooriya

How does the HVDC link benefit Sri Lanka specifically?

For Sri Lanka, the HVDC link allows the export of 14% of its excess power during December when hydro and coal generation are high. It also enables the import of energy from India during periods of hydropower variability. According to a 2018 report by the National Renewable Energy Lab, the 500MW HVDC link could save Sri Lanka USD 180 million annually by decreasing production costs by 35%.

What advantages does HVDC transmission have over traditional HVAC systems?

HVDC transmission is preferred over HVAC due to its cost-effectiveness and efficiency in transferring power over long distances. HVDC systems have minimal energy loss because they do not experience capacitive charging and discharging as there is no change in voltage polarity causing displacement current to flow through the capacitance of the transmission line. They can interconnect asynchronous grids, which is vital when countries use different voltage levels and frequencies. Additionally, HVDC systems require fewer cables, reducing cable costs. In terms of initial investment, HVDC systems will cost more than traditional systems. This is because of costs associated with converters and other associated devices. However, over a critical distance where both HVDC and HVAC costs breakeven, which is about 75km for submarine cables and 700km for overhead lines, the HVDC transmission become way more economical than traditional systems.

Could you provide some historical context on HVDC systems and their evolution?

Absolutely. High Voltage Direct Current (HVDC) systems have a fascinating history that spans over seven decades. The journey began in 1954 with the first modern HVDC system between Gotland and Sweden, which had a capacity of 20MW at 100kV DC over a 96km submarine cable. This pioneering project set the stage for more ambitious cross-border connections. For instance, in 1961, England and France established the first cross-channel HVDC link, which initially had a capacity of 160MW at 100kV DC and was later expanded to a 2x1000MW, 270kV DC link in 1986. Over the years, several significant projects have been completed, such as the Volgograd-Donbass link in 1972, which connected Russia and Ukraine with a 750MW, 400kV DC line over 450km, and Brazil’s Itaipu HVDC link in 1984, which transmitted 6300MW at 600kV DC over 800km from hydroelectric generators to São Paulo.

At the beginning, HVDC systems relied on a thyristor-based Line Commutated Converters (LCC), which were costly and required a lot of harmonic filtering but the introduction of an IGBT-based Voltage Source Converters (VSC) in 1999 revolutionised the technology. VSCs are more controllable, cost-effective, and equipped with Black start capabilities i.e. allowing grids to restart without external power. LCCs did not have that capability. The first VSC-based transmission was implemented in Gotland, Sweden, with a capacity of 50MW at 800kV DC. This advancement has led to the development of projects such as Borwin1, which began in 2009 and was commissioned in 2015 to transport power from offshore wind farms to Germany. The United Kingdom has been active in this field, completing the East-West interconnector in 2012, a submarine link connecting Ireland and Wales, as well as the North Sea Link with Norway and the Viking Link connecting the UK and Denmark. The largest wind farm in the world, Dogger Bank, will soon connect to the UK grid via multiple HVDC links.

India Sri Lanka grid map

China and India have embraced HVDC for long-distance power transmission and integrating renewable energy into their main grids. Notable projects include China’s Xian Jiba-Shanghai link and India’s Talcher-Kolhar link. These developments have paved the way for the concept of ‘supergrid’. The supergrid aims to connect international borders and economic zones, facilitating energy trading and supporting global decarbonisation efforts. Proposed supergrids include the European supergrid and the North African supergrid, which are expected to harness renewable energy resources for Europe. Ambitious initiatives like China’s Global Energy Initiative (GEI) and India’s One Sun One World One Grid plan aim to create a global energy market, encouraging countries to participate early to secure their future energy supply. Despite technical challenges, such as managing DC line faults, ongoing research is addressing these issues, ensuring the reliability and efficiency of HVDC systems.

So what are these technical challenges associated with HVDC transmission that you are conducting research for?

HVDC transmission systems face several technical challenges, particularly in managing DC line faults. DC systems have low inductances, so fault currents can rise and propagate rapidly, reaching damaging levels within just a few milliseconds - around 5ms. This puts a demand on the system design engineers to come up with extremely fast fault detection methods to detect and isolate the faulty cable to maintain the balance and continuity of service in the unaffected parts of the grid before fault current reaches damaging levels. Traditional protection methods, such as di/dt or dv/dt-based algorithms, they operate by detecting the gradient of the fault current or voltage, but these can be sensitive to noise and lead to false positives. There is another method called the differential protection method. These methods compare the currents at two ends of a transmission line to detect a fault. However, these again are sensitive to variables like transmission line’s length, time delays, and communication errors, requiring the relay engineer to manually set different thresholds for different line lengths.

To address these challenges, we at Staffordshire University have been investigating advanced techniques like travelling wave-based protection and discrete wavelet transform based protection method. The travelling wave method detects faults by analysing electric disturbances that propagate along transmission lines at light speed of light. Imagine a stone thrown into a pond and its ripples spread outwards from the point of contact. Likewise, after a fault, the electric disturbances propagate along the transmission line and because these propagate at the speed of light, a fault can be rapidly detected by analysing the ripples. Also, even as you can trace back the location of the stone dropped in the water by following back the ripples, the fault’s location can also be traced back by analysing its wavelength.

Secondly wavelet transforms offer a time-scaled representation of a signal by decomposing the signal into shifted and scaled versions of the original signal. This method is analogous to human voice. The human voice comprises many frequencies. The high frequency component is responsible for noise. Meaning should there be a fault in your voice, it is revealed in the high frequency component. Think of it as a singer on a stage whose voice breaks down.You will hear an off-tuned high-pitched noise. By simply extracting the high frequency component we can detect a fault at a very early stage giving us enough time to expedite the protection mechanisms. Also, by matching it with the wavelet coefficients it is also possible to classify the fault by a simple signal processing algorithm. Both techniques contribute in monitoring Multi-terminal HVDC grids. These methods require high-speed computational systems to detect faults and send disengagement signals within milliseconds. My team at Staffordshire University is using the OPAL-RT Real-Time Simulator for this purpose, conducting Hardware-in-the-Loop testing to monitor and control the live grid. This research is crucial for enhancing the reliability and efficiency of HVDC systems.

Last year the theoretical work on Wavelet transforms was done by Jashandeep Kaur, a BEng student of mine who graduated last July. He was awarded the IET Edward Riddell Shied. Real time simulation and HIL research with OPAL-RT is currently being conducted by a third-year student Akash Sovis. Both brilliant and hardworking individuals who burnt both ends of the candle with me too deserve the credit of our achievements.
