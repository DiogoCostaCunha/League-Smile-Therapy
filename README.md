# League of Legends Smile Therapy 😁

This is the code behind the **League of Legends mod** shown in [this video](https://youtu.be/I3m8nhHngs4)! 
Either you smile and fill that little green bar… or the client gets terminated. 

> Who knew League players were even capable of joy?

<p align="center">
  <img src="https://github.com/user-attachments/assets/0fcd93be-55c4-47c9-aef8-12a64742b6d0" alt="thumbnail" width="45%" />
  <img src="https://github.com/user-attachments/assets/c86ef112-4659-4932-8917-e10db1dc616b" alt="still" width="45%" />
</p>

## 🧠 How It Works

The script uses real-time **facial landmark detection** to check if you're smiling. If you stop smiling, the progress bar starts draining. Let it hit zero… and the League client is terminated.

To understand the whole setup, [**watch the video first**](https://youtu.be/I3m8nhHngs4)—it’ll make things clearer!


## ⚙️ Setup Instructions

> Requires Python **3.10+**

1. **Clone** or download this repository.
2. Create and activate a [python virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
3. Install the requirements ```pip install -r requirements.txt```
4. Download the [face landmarks](https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat) and place it on the root folder.
5. Execute ```python smile_detector.py``` and you're ready to go! Enjoy the fun—or the despair!

## 🛠 Customization

You can tweak the script’s behavior using the config.json file.
- ```decay_rate```: How fast the bar goes down when you're not smiling. Higher = harder.
- ```fill_rate```: How fast the bar fills up when you're smiling. Higher = easier.
- ```mouth_ratio_threshold```: Minimum mouth openness to count as a smile. Higher = stricter.
- ```eyes_ratio_threshold```: Minimum eye openness to count as a smile. Higher = stricter.

Also, the smile windows are draggable and resizable!

## ⚠️ Disclaimer

This is a fun, experimental tool.
I’ve never had issues running it during League matches, but I can't guarantee your client or match won’t crash or misbehave. I can't also ensure that you won't face problems with Riot anticheat software, although I also never had those.
**Use at your own risk.**

## Support My Channel 🚀

I make weird and wonderful projects at the crossroads of AI, hardware, and chaotic fun.

If you enjoyed this and want more, please consider [subscribing to my YouTube channel](https://www.youtube.com/channel/UCqnIZIGyH6NgJ8OkJAvZyKg?sub_confirmation=1). Your support helps me keep doing this stuff!
