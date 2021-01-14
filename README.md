# Dolphins recognition challenge
> The challenge has two parts:


!["Croatian AI League"](https://raw.githubusercontent.com/cro-ai-league/dolphins-recognition-challenge/master/docs/images/AILeague_logo-800x452.png)

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

```python
from dolphins_recognition_challenge.datasets import get_dataset

train_ds, val_ds = get_dataset("segmentation")

type(train_ds)
```




    torch.utils.data.dataloader.DataLoader



## Sponsors

Here they go...

