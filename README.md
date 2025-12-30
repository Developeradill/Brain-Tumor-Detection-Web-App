## 📌 Overview

This project is an **AI-based web application** that detects **brain tumors from MRI images** using a **Convolutional Neural Network (CNN)**.
The system allows users to upload MRI images and instantly receive detection results through a simple and user-friendly web interface.

This project focuses on **model deployment, web integration, and real-time usability**, making it suitable for **research, academic, and demonstration purposes**.

---

## 🚀 Features

* Upload MRI images through a web interface
* Automatic **Tumor / Normal** classification
* Deep learning–based CNN model
* Flask backend for model serving
* Clean and responsive UI
* Optional **voice feedback** for prediction results

---

## 🛠 Technologies Used

* **Python**
* **TensorFlow / Keras**
* **Flask**
* **HTML, CSS, JavaScript**
* **OpenCV**
* **NumPy**

---

## 🧠 Model Information

* Model Type: CNN (Convolutional Neural Network)
* Input Image Size: **224 × 224**
* Dataset Source: **Public MRI Brain Tumor Dataset (Kaggle)**
* Model Training: Dataset preprocessing and training inspired by Kaggle resources
* Model Deployment & Web Integration: **Done by me**

> ⚠️ This project emphasizes **deployment and application development**, not dataset ownership.

---

## 📁 Project Structure

```
brain-tumor-detection-web-app/
│
├── app.py                  # Main Flask application
├── model/
│   └── brain_tumor.h5       # Trained deep learning model
│
├── templates/
│   └── index.html           # Web UI
│
├── static/
│   └── style.css            # Styling files
│
├── uploads/                 # Uploaded MRI images
│
├── requirements.txt         # Python dependencies
├── README.md
└── LICENSE
```

---

## ⚙️ Installation Guide (Step-by-Step)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Developeradill/Brain-Tumor-Detection-Web-App.git
cd Brain-Tumor-Detection-Web-App
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Place the Model File

Ensure the trained model file is placed correctly:

```
model/brain_tumor.h5
```

⚠️ If your model name is different, update it inside `app.py`.

---

### 5️⃣ Run the Application

```bash
python app.py
```

---

### 6️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 How to Use

1. Open the web application
2. Upload an MRI image
3. Click **Predict**
4. View tumor detection result
5. (Optional) Listen to voice output

---

## 📌 Requirements.txt Example

```
flask
tensorflow
keras
opencv-python
numpy
pillow
```

---

## 🔮 Future Improvements

* Multi-class tumor classification
* Improved accuracy using fine-tuning
* Cloud deployment (AWS / Azure)
* Mobile-friendly UI
* Doctor-oriented reporting system

---

## 👨‍💻 Author

**Adil Khan**
Computer Systems Engineer
AI & Web Application Developer

---

## 📜 License

This project is licensed under the **MIT License**.

---

⭐ *If you find this project helpful, feel free to star the repository!*
