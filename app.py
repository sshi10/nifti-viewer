from flask import Flask, render_template, send_file, make_response
import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import io
import os
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

# Load and process the nifti file
def load_nifti(filename):
    img = nib.load(filename)
    data = img.get_fdata()
    return data

def get_slice_image(data, axis, slice_index):
    if axis == 'axial':
        slice_data = data[:, :, slice_index]
    elif axis == 'sagittal':
        slice_data = data[slice_index, :, :]
    elif axis == 'coronal':
        slice_data = data[:, slice_index, :]

    plt.figure(figsize=(6, 6))
    plt.imshow(np.rot90(slice_data), cmap='gray')
    plt.axis('off')
    
    # Save the plot to an in-memory buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    buf.seek(0)
    return buf

# Load nifti file and store data
nifti_data = load_nifti('data/tcga_17_z011_0000.nii')

@app.route('/')
def index():
    return render_template('index.html', max_slices={
        'axial': nifti_data.shape[2],
        'sagittal': nifti_data.shape[0],
        'coronal': nifti_data.shape[1]
    })

@app.route('/view/<string:view>/<int:slice_index>')
def view_image(view, slice_index):
    buf = get_slice_image(nifti_data, view, slice_index)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='localhost', port=8000)