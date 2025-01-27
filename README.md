## **CT Scan Viewer**

A web-based application for visualizing medical CT scan slices in **axial**, **sagittal**, and **coronal** views. The viewer supports interactive navigation through slices, dynamic resizing for responsive displays, and efficient preloading of medical images for a smooth user experience.

---

### **Demo**

<div>
    <a href="https://www.loom.com/share/3b9c65b9edcb4534975aea915e06f72e">
    </a>
    <a href="https://www.loom.com/share/3b9c65b9edcb4534975aea915e06f72e">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/3b9c65b9edcb4534975aea915e06f72e-0699934b0a07d77b-full-play.gif">
    </a>
  </div>

---

### **Getting Started**

#### **Prerequisites**
- Python 3.6 or higher
- Pip for dependency management
- A web browser (e.g., Chrome, Firefox)

#### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/sshi10/nifti-viewer.git
   cd nifti-viewer
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   - **On macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - **On Windows**:
     ```bash
     venv\Scripts\activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Place your NIfTI file (`.nii` or `.nii.gz`) in the `data/` directory.

#### **Running the Application**
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

---

### **Usage**

#### **Navigation**
- **Views**:
  - Switch between **axial**, **sagittal**, and **coronal** views using the buttons.
- **Slice Scrolling**:
  - Use the mouse scroll or trackpad to navigate through slices.

---

### **Technology Stack**
- **Backend**: [Flask](https://flask.palletsprojects.com/) for the backend framework..
- **Frontend**: HTML5 and JavaScript for interactive visualization.
- **Image Processing**: [Nibabel](https://nipy.org/nibabel/) and [Matplotlib](https://matplotlib.org/).

---

### **File Structure**
```
project-root/
|
├── app.py               # Main Flask application
├── templates/
│   └── index.html       # Frontend HTML file
├── static/
│   └── style.css        # CSS styles (if applicable)
├── data/
│   └── example.nii      # Example NIfTI file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

### **License**
This project is licensed under the MIT License - see the LICENSE file for details.

---

### **Future Enhancements**
- Add multiview display functionality to show all views simultaneously.
- Include hotkey navigation
- Image upload