# League of Legends Smile Therapy

The Code for the League Mod used in [this video](https://youtu.be/I3m8nhHngs4)! Either you smile and fill that little green bar... or you’ll be forced to carry the bad vibes out of the Rift with you (your client gets terminated 💀). 

![thumbnail_2](https://github.com/user-attachments/assets/0fcd93be-55c4-47c9-aef8-12a64742b6d0)

![Still 2025-04-21 143659_2 98 1](https://github.com/user-attachments/assets/c86ef112-4659-4932-8917-e10db1dc616b)

I advice you to check the video first to have an idea of how the script is supposed to work.


## Setup
You'll need at least Python 3.10 installed to be able to setup the following.

1. Clone or download the repository.
2. Set up a [python virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/), activate it, and install requirements.txt
3. Download the [face landmarks](https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat) and place it on the root folder of the git repository
4. Run 'python smile_detector.py' and you're ready to go! Enjoy the fun—or the despair!

## Customization
You can customize the script functioning in config.json. The parameters there mean the following:
- decay_rate: the rate at which the bar empties when you're not smiling. Higher value makes it more difficult.
- fill_rate: the rate at which the bar fills up when you're smiling. Higher value makes it easier.
- mouth_ratio_threshold: affects how wide your mouth must be for the smile to count. Higher value makes it more difficult.
- eyes_ratio_threshold: affects how wide your eyes must be for the smile to count. Higher value makes it more difficult.

## Disclaimer ⚠️

I take no responsibility for any problem that arises from using this application while playing League of Legends. I have never had any problem since I have started using it, but I can't ensure anything in this matter. Use at your own risk.

## Support My Channel 🚀

I'm on a quest to create innovative and funny content, exploring the intersections of AI, software, and hardware! If you're intrigued, please consider [subscribing to my YouTube channel](https://www.youtube.com/channel/UCqnIZIGyH6NgJ8OkJAvZyKg?sub_confirmation=1) to stay updated!
