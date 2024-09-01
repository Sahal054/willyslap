#SlapRock
SlapRock is a fun and interactive game built using Python and OpenCV where you control a virtual hand to slap Chris Rock, reminiscent of the famous Oscars incident. The game utilizes computer vision to detect your hand movements, allowing you to move an object across the screen to catch Chris Rock's face as it randomly spawns. The challenge is to react quickly and slap his face before it disappears!

Features
Hand Tracking: The game uses OpenCV to detect and track your hand movements in real-time.
Random Spawning: Chris Rock's face appears randomly on the screen, keeping you on your toes.
Scoring System: Earn points for every successful slap.
Fun and Engaging: A simple yet entertaining game with a humorous twist.
Installation
To play SlapRock, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/SlapRock.git
cd SlapRock
Install Dependencies: Ensure you have Python installed. Then, install the required libraries:

bash
Copy code
pip install -r requirements.txt
Run the Game:

bash
Copy code
python slaprock.py
How to Play
Setup: Make sure your webcam is connected and positioned correctly to detect your hand movements.
Start the Game: Run the game script, and you'll see Chris Rock's face appear randomly on the screen.
Slap Chris Rock: Move your hand to the target and slap his face before it disappears. Your score increases with each successful slap.
Challenge Yourself: Try to get the highest score by slapping Chris Rock as many times as possible before time runs out.
Requirements
Python 3.7+
OpenCV
NumPy
