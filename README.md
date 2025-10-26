# RecognitionV1 🖐️
A real-time hand gesture recognition system that translates gestures into text responses such as “Hello”, “Yes”, “No”, “Stop”, "OK" and “Love You”.


## 🧠 Overview
**RecognitionV1** is a computer vision project built using Python, OpenCV and MediaPipe.  
It captures hand gestures through the webcam, processes them, and predicts the corresponding gesture in real-time using a trained model.


## 🎯 Features
- 📷 Real-time gesture capture via webcam  
- 🧩 Dataset generation using keyboard shortcuts  
- 🖐️ Recognizes 6 hand gestures:
  - ✋ Palm Up → `Hello`
  - 👍 Thumbs Up → `Yes`
  - 👎 Thumbs Down → `No`
  - ✊ Closed Fist → `Stop`
  - 🤟 “I Love You” gesture → `Love You`
  - 👌 "Ok" guesture -> 'Ok'
- 💾 Saves gesture samples into CSV format
- 🧠 Model training with scikit-learn



## 🧰 Project Structure

RecognitionV1/
│
├── Dataset/
│   ├── all_gestures.csv
│   ├── Hello.csv
│   ├── Love you.csv
│   ├── No.csv
│   ├── Ok.csv
│   ├── Stop.csv
│   ├── Yes.csv
│
├── signenv/                 # Virtual environment (ignored in Git)
│
├── main.py                  # Runs real-time gesture recognition
├── train.py                 # Trains the model and saves it as .pkl
├── model.py                 # Contains model loading / prediction functions
├── merge.py                 # Merges all gesture CSVs into one dataset
├── signLan_model.pkl        # Saved model file
└── requirements.txt         # Dependencies list
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/RecognitionV1.git
cd RecognitionV1
```

### 2️⃣ Create a Virtual Environment (optional but recommended)
```bash
python -m venv signenv
signenv\Scripts\activate
```

### 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

---

## 📸 How to Use

### **1. Collect Gesture Samples**
Run:
```bash
python train.py
```
- Press **S** → to save image sample  
- Press **Q** → to quit webcam  

This generates gesture data and stores it inside the `Dataset` folder.

---

### **2. Train the Model**
Run:
```bash
python model.py
```
This script trains a classifier using your dataset and saves it as `signLan_model.pkl`.

---

### **3. Run Real-Time Recognition**
Run:
```bash
python main.py
```
Now show your gestures to the webcam and watch it display:
> “Hello”, “Yes”, “No”, “Stop”, or “Love You”

---

## 🧩 Requirements
See [`requirements.txt`](#requirements).

---

## 📦 requirements.txt
```
opencv-python
mediapipe
pandas
numpy
scikit-learn
```

---

## 💡 Notes
- Make sure your webcam is properly connected.
- You can add more gestures by updating `train.py` and appending new CSVs to the dataset.
- Adjust model parameters in `model.py` for higher accuracy.

---

## 👨‍💻 Author
**Vishal Thakur**  
Inspired by Tony Stark’s vision of merging AI with innovation ⚙️  
*“Sometimes you’ve gotta run before you can walk.”*