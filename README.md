# Dolphins recognition challenge
> The challenge has two parts:


!["Croatian AI League"](notebooks/images/AILeague_logo-800x452.png)

## Tutorial

The easiest way to start and sbmit your solution is to open the following tutorial on Colaboratory from Google: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cro-ai-league/dolphins-recognition-challenge/blob/master/notebooks/00_tutorial/DolphinsTutorial.ipynb)

## Leaderboard

The leaderboard will be periodically updated to reflect new sumbissions.
> Notice:The leaderboard is generated using validtion set and will most likely be different when evaluated at the end of the contest using test dataset due to overfitting.




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>alias</th>
      <th>date</th>
      <th>submitted_iou</th>
      <th>calculated_iou</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>prvi_pokušaj</td>
      <td>2021-01-13 14:29:59.372504</td>
      <td>0.44925</td>
      <td>0.449246</td>
    </tr>
  </tbody>
</table>
</div>



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

