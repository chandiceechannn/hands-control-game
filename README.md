# 🎮 Hand Gesture Controller for Web Games (Subway Surfers / Temple Run)

## 📌 Description

This project is a **hand gesture-based game controller** that uses your webcam to control games in real time.
By leveraging **computer vision**, your hand movements can replace keyboard input.

It works great with browser games like:

* Subway Surfers (Poki web)
* Temple Run (poki Web)

No keyboard needed — just use your hand ✋

---

## 🚀 Features

* ✌️ Move right using two fingers
* ☝️ Move left using index finger
* ✊ Slide using a fist
* ✋ Jump using open hand
* Real-time hand tracking via webcam
* Low-latency response

---

## 🧠 Technologies Used

* `OpenCV` → Webcam video capture
* `MediaPipe` → Hand tracking & landmark detection
* `PyAutoGUI` → Keyboard input automation
* `Python`

---

## 🎮 Gesture Mapping

| Gesture             | Action     | Key |
| ------------------- | ---------- | --- |
| ✌️ (Index + Middle) | Move Right | →   |
| ☝️ (Index only)     | Move Left  | ←   |
| ✊ (Fist)            | Slide      | ↓   |
| ✋ (Open hand)       | Jump       | ↑   |

---

## ⚙️ How to Run

### 1. Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

### 2. Run the Script

```bash
python subway.py
```

### 3. Open the Game

Go to:

* https://poki.com (play Subway Surfers or Temple Run)

---

## 📷 How to Use

1. Turn on your webcam
2. Place your hand in front of the camera
3. Perform gestures based on the controls
4. Click on the game window (important!)
5. Play the game using your hand 🎉

---

## ⚡ Tips for Better Performance

* Use good lighting conditions
* Keep background simple (avoid clutter)
* Lower camera resolution for faster processing
* Set `pyautogui.PAUSE = 0` to reduce delay

---

# enjoyy !!
