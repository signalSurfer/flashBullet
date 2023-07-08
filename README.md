# flashBullet <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"> 
🧠Study time! </br>
flashBullet is a simple script to create your own push notification flash cards using [pushbullet](https://www.pushbullet.com/) and a python dictionary and random choice. </br></br>
# After signing into a pushbullet account [Get your API key here](https://www.pushbullet.com/#settings/account).
You need a pro subscription to use the API.  - Looking into a free alternative</br>
Click [Create Access Token]</br>
paste your access token in the API_KEY variable in the quotes, overwriting yourapikeyhere.</br> 


# Here's how it works:</br>
<ol>
  <li>set up your environment</li>
  <ul>
    <li>Install Python</li>
    <li>pip install pushbullet.py</li>
  </ul>
  <li>copy the script</li>
  <ul>
    <li>plug in your API key</li>
  </ul>
  <li>fill in a dictionary {'Key=Title':'Value=body'}</li>
  <li>schedule the script to run, or slap it in a timed loop.</li>
  <li>get periodic push notifications relevant to your studies!</li>
</ol>

I plan on making dictionaries as I study new topics, Please feel free to pull request your own.


# ChatGPT will make a dictionary for you, here is an example prompt:</br>
<i>Please create a python dictionary with keys that are vocabulary words, and values are definitions of the keys. There should be at least _______ key value pairs, and they should all be _______ themed.</i></br></br>
![exampleGPT](https://github.com/signalSurfer/flashBullet/assets/130820868/8305acf5-0c24-4b55-87c6-74b9c8097cda)
