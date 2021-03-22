# Dolphins recognition challenge



!["Croatian AI League"](https://raw.githubusercontent.com/cro-ai-league/dolphins-recognition-challenge/master/docs/images/AILeague_logo-800x452.png)

## Tutorial

The easiest way to start and submit your solution is to open the following tutorial on Colaboratory from Google.
Click the button below to open a tutorial on Google Colaboratory. Clicking the button will open a Google Collaborative website with a tutorial containing detailed instructions and tips on how to train the model. By following the tutorial cell by cell, you will make your first model and participate in the challenge.
[!["Open In Colab"](https://raw.githubusercontent.com/cro-ai-league/dolphins-recognition-challenge/add_image_button/notebooks/images/open_in_colab_button.svg)](https://colab.research.google.com/github/cro-ai-league/dolphins-recognition-challenge/blob/master/notebooks/00_tutorial/DolphinsTutorial.ipynb)

## Intro

The challenge has two parts:
- instance segmentation of dolphins in the photo (February 18th - June 4th 2021), and
- recognition of an individual dolphin from the photo (June 5th - September 3th 2021). 

## Legal

- Official rules (in Croatian) can be found at the following  [link](https://cro-ai-league.cisex.org/Rules.html).

- Privacy notice (in Croatian) can be found at the following  [link](https://cro-ai-league.cisex.org/Privacy_notice.html).



## Leaderboard

<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/medal-2.jpeg" alt="medal">

The leaderboard will be periodically updated to reflect new sumbissions.
The leaderboard is generated using validation set and will most likely be different when evaluated at the end of the contest using test dataset due to overfitting.
        alias        date                          submitted_iou    calculated_iou
    --  -----------  --------------------------  ---------------  ----------------
     1  stokic       2021-02-21 18:51:53.232539          0.43552               nan
     2  firstML      2021-02-28 09:55:59.155951          0.42529               nan
     3  rangoiv_0.0  2021-03-11 21:18:19.755089          0.41769               nan
     4  testy        2021-03-12 15:06:14.210987          0.39001               nan


## Local install

You can also work on your own personal computer or cloud by installing our [pip package](https://pypi.org/project/dolphins-recognition-challenge/) and downloading the data directly using the following command:

`pip install dolphins-recognition-challenge`

### How to use

The dataset is prepared for use with PyTorch, although it is easy to prepare it for other frameworks. To use it with PyTorch, install the PIP package above and import it as follows:

```python
from dolphins_recognition_challenge.datasets import get_dataset

train_ds, val_ds = get_dataset("segmentation")
```

The easiest way is to start is by downloading the same [tutorial](https://github.com/cro-ai-league/dolphins-recognition-challenge/blob/master/notebooks/00_tutorial/DolphinsTutorial.ipynb) Jupyter notebook mentioned above.

## Discussions

[Discussions](https://github.com/cro-ai-league/dolphins-recognition-challenge/discussions) are hosted on Github, together with the complete source code of the challenge. There you can ask questions and discuss any matter you like.

## Organizers

##### 

<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/cisex_logo.png" alt="CISEx" width="150" style="max-width: 150px">

[CISEx](https://www.cisex.org/) is an association of independent software exporters that gathers over 280 members, mostly companies from IT sector oriented towards global market. Our main goal is to strengthen the position of IT sector in Croatia by supporting software production, export and entrepreneurship, creating new jobs and positioning our members on the global market. It serves as a platform for growth and development of all our members, joint appearance on the domestic and foreign markets, exchange of experiences and mutual cooperation.  

##### 

<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/bwi_logoen.png" alt="Blue World Institute" width="150" style="max-width: 150px">

[The Blue World Institute of Marine Research and Conservation](https://www.blue-world.org/) works to protect the marine environment in the Adriatic Sea. To that purpose, the Blue World Institute operates three programmes – research, education, and conservation. Our research focuses mainly on large marine vertebrates (dolphins and whales, sea turtles, sharks and giant devil rays) informing our education activities and conservation projects. We work from the Adriatic islands of Lošinj, Murter and Vis, with the local communities, and collaborate nationally, regionally and internationally to advance sustainable marine management and environmental sustainability in the Mediterranean Basin.  

##### 

<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/CroAI-logo.jpg" alt="CroAI" width="150" style="max-width: 150px">

[CroAI](https://www.croai.org/), the Croatian Artificial Intelligence Association, was founded in 2019 and brings together leading companies and startups in the field of AI in Croatia. CroAI seeks to position Croatia as a country of unique opportunities for the development of human-centric AI through a culture of dialogue between entrepreneurs and decision makers at the national and European level.  


## Sponsors

##### 

<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/01_Infobip_logo_horizontal_rgb_color.png?v=2" alt="Infobip" width="150" style="max-width: 150px">
  
[Infobip](https://www.infobip.com/) is a global cloud communications platform that enables businesses to build connected experiences across all stages of the customer journey. Accessed through a single platform, Infobip’s omnichannel engagement, identity, security and contact center solutions help clients and partners overcome the complexity of consumer communications, grow their business and increase loyalty. With over a decade of industry experience, Infobip has expanded to include 65+ offices on six continents offering natively built technology with the capacity to reach over seven billion mobile devices and ‘things’ in 190+ countries connected directly to over 650 telecom networks.  
  
##### 

<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/Photomath-logo-RGB.png?v=2" alt="Photomath" width="200" style="max-width: 200px">

[Photomath](https://photomath.app/) is a fast-growing EdTech company whose mobile app is the #1 app in the world to learn math. Powered by advanced machine learning technology, app instantly scans, accurately solves, and intuitively explains printed and handwritten math problems to users through step-by-step explanations. With over 220 million downloads globally and tens of millions of users worldwide every month, Photomath is the most popular mobile application from Croatia and one of the most popular educational apps of all times. The Photomath team in Zagreb has grown to over 100 employees and more than 100 students working on content creation, and they also have a team of a dozen people in Silicon Valley, USA. Photomath’s mission is to democratize education through the use of artificial intelligence and software-generated educational content. For their ambitious plans, they bring together top experts who have the opportunity to work on a global product and gain unique technological knowledge and experience. In 2021, they plan further investments and employment, especially in the segment of software development and artificial intelligence.  
  
##### 

<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/PDC-logo-horizontal-transparent.png?v=2" alt="Porsche Digital Croatia" width="250" style="max-width: 250px">

[Porsche Digital Croatia](https://infinum.com/ventures/porsche-digital-croatia/) is a joint venture formed by [Infinum](https://infinum.com/), the leading software design and development company in Croatia, and [Porsche Digital](https://www.porsche.digital/), a subsidiary of the German sports car manufacturer. The goal of this company is to be the hub of digital innovation and high-tech solutions in the automotive sector, and the main mission is to find and develop new digital business models and optimize existing products. Their teams of talented professionals are focused on technological innovation and are passionate about software development and design, machine learning and artificial intelligence.

