# ikachan-banner-roulette

This app update your Twitter profile banner with a random ikachan banner. There are 52144048642943865156821842963009777645716183826377660210582528000 patterns!

![banner_1](./images/banner_1.png)
![banner_2](./images/banner_2.png)
![banner_3](./images/banner_3.png)

## Twitter API
You need to get and fill your account tokens to 'account.json'.

```
{
  "CONSUMER_KEY": "",
  "CONSUMER_SECRET": "",
  "ACCESS_TOKEN": "",
  "ACCESS_TOKEN_SECRET": ""
}
```

## Cron
Use cron, if you want to update your banner periodically.

```
0 1-23/2 0 0 0 $HOME/.pyenv/shims/python $HOME/app/ikachan-banner-roulette/main.py
```
