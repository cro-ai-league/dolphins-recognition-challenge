# Dolphins recognition challenge



!["Croatian AI League"](https://raw.githubusercontent.com/cro-ai-league/dolphins-recognition-challenge/master/docs/images/AILeague_logo-800x452.png)

## Intro

The challenge has two parts:
- instance segmentation of dolphins in the photo, and
- recognition of an individual dolphin from the photo. 

## Tutorial

The easiest way to start and sbmit your solution is to open the following tutorial on Colaboratory from Google: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cro-ai-league/dolphins-recognition-challenge/blob/master/notebooks/00_tutorial/DolphinsTutorial.ipynb)

## Leaderboard

The leaderboard will be periodically updated to reflect new sumbissions.
> Notice:The leaderboard is generated using validtion set and will most likely be different when evaluated at the end of the contest using test dataset due to overfitting.

        alias         date                          submitted_iou    calculated_iou
    --  ------------  --------------------------  ---------------  ----------------
     1  prvi_pokušaj  2021-01-13 14:29:59.372504          0.44925          0.449246


## Local install

You can also work on your own personal computer or cloud by installing a PIP package and downloading the data directly using the following command:

`pip install dolphins-recognition-challenge`

### How to use

The dataset is prepared for use with PyTorch, although it is easy to prepare it for other frameworks. To use it with PyTorch, install the PIP package above and import it as follows:

```
from dolphins_recognition_challenge.datasets import get_dataset

train_ds, val_ds = get_dataset("segmentation")

type(train_ds)
```




    torch.utils.data.dataloader.DataLoader



## Rules & privacy notice

- Official rules can be found at the following  [link](https://cro-ai-league.github.io/dolphins-recognition-challenge/Rules.html).

- Privacy notice can be found at the following  [link](https://cro-ai-league.github.io/dolphins-recognition-challenge/Privacy_notice.html).



## Organizers


<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/cisex_logo.png" alt="CISEx" width="150" style="max-width: 150px">

[CISEx](https://www.cisex.org/) is an association of independent software exporters that gathers over 280 members, mostly companies from IT sector oriented towards global market. Our main goal is to strengthen the position of IT sector in Croatia by supporting software production, export and entrepreneurship, creating new jobs and positioning our members on the global market. It serves as a platform for growth and development of all our members, joint appearance on the domestic and foreign markets, exchange of experiences and mutual cooperation

<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/bwi_logoen.png" alt="Blue World Institute" width="150" style="max-width: 150px">

[The Blue World Institute of Marine Research and Conservation](https://www.blue-world.org/) works to protect the marine environment in the Adriatic Sea. To that purpose, the Blue World Institute operates three programmes – research, education, and conservation. Our research focuses mainly on large marine vertebrates (dolphins and whales, sea turtles, sharks and giant devil rays) informing our education activities and conservation projects. We work from the Adriatic islands of Lošinj, Murter and Vis, with the local communities, and collaborate nationally, regionally and internationally to advance sustainable marine management and environmental sustainability in the Mediterranean Basin.


## Sponsors
      
<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/01_Infobip_logo_horizontal_rgb_color.png" alt="Infobip" width="150" style="max-width: 150px">
  
[Infobip](https://www.infobip.com/) is a global cloud communications platform that enables businesses to build connected customer experiences across all stages of the customer journey at scale, with easy and contextualized interactions over customers’ preferred channels. Accessed through a single platform, Infobip’s omnichannel engagement, identity, user authentication security and contact center solutions help clients and partners overcome the complexity of consumer communications, grow their business and increase loyalty– all in a fast, secure and reliable way. With over a decade of industry experience, Infobip has expanded to include 68+ offices on six continents offering natively built technology with the capacity to reach over seven billion mobile devices and ‘things’ in 190+ countries connected directly to over 600 telecom networks. The company serves and partners with leading mobile operators, messaging apps, banks, social networks, tech companies, and aggregators.


<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/Photomath-logo-RGB.png" alt="Photomath" width="225" style="max-width: 225px">

[Photomath](https://photomath.app/) is a fast-growing EdTech company whose mobile app is the #1 app in the world to learn math. Powered by advanced machine learning technology, the app instantly scans, accurately solves, and intuitively explains printed and handwritten math problems to users through step-by-step explanations.
 
With over 200 million downloads globally and 25 million monthly users, Photomath is the most popular mobile application from Croatia and one of the most popular educational apps of all times. Since its launch in 2014, this award-winning app has topped App Store & Google Play Store education charts and Apple has recently declared it the application of the day.
 
As math is an increasingly crucial skill, particularly as problem-solving and quantitative analysis become prerequisites for many occupations of the future, Photomath is constantly expanding what the app can do and the types and quality of the content. Their mission is to revolutionize learning math and help students across the globe gain math superpowers.
 
Since 2016, the company has grown from 30 to almost 200 people and plans to further grow rapidly, especially expanding its engineering teams with experienced experts in web development, mobile app development and machine learning.


<img src="https://github.com/cro-ai-league/dolphins-recognition-challenge/raw/master/docs/images/PDC-logo-horizontal-transparent.png" alt="Porsche Digital Croatia" width="250" style="max-width: 250px">

[Porsche Digital Croatia](https://infinum.com/ventures/porsche-digital-croatia/) is a joint venture formed by [Infinum](https://infinum.com/), the leading software design and development company in Croatia, and Porsche Digital, a subsidiary of the German sports car manufacturer. The goal of this company is to be the hub of digital innovation and high-tech solutions in the automotive sector, and the main mission is to find and develop new digital business models and optimize existing products. Their teams of talented professionals are focused on technological innovation and are passionate about software development and design, machine learning and artificial intelligence.

