[![GitHub stars](https://img.shields.io/github/stars/amine0110/Medical-Conversions)](https://github.com/amine0110/Medical-Conversions/stargazers) [![GitHub forks](https://img.shields.io/github/forks/amine0110/Medical-Conversions)](https://github.com/amine0110/Medical-Conversions/network) [![GitHub issues](https://img.shields.io/github/issues/amine0110/Medical-Conversions)](https://github.com/amine0110/Medical-Conversions/issues) [![GitHub license](https://img.shields.io/github/license/amine0110/Medical-Conversions)](https://github.com/amine0110/Medical-Conversions) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nibabel) [![YouTube Video Views](https://img.shields.io/youtube/views/zXPcH_s0NtM?style=social)](https://youtu.be/zXPcH_s0NtM) ![GitHub watchers](https://img.shields.io/github/watchers/amine0110/Medical-Conversions?style=social)

# Convert Medical Images (dicom & nifti)
[The landing page](https://pycad.co/pycad-convert/)

This simple tool allows you to:
- Convert `jpg/png` images into `dicom`.
- Convert `dicom` into `jpg` images.
- Convert `nifti` files into `dicom` series.
- Convert `dicom` series into `nifti` files

And all this conversions can be done both, in one file or in a whole directory.

To run the app, you must have `Python` installed on your machine. You will also need some prerequisites, which you can easily install from the file provided with this repo. Please follow these steps to ensure that you can launch the app without issue.

1. Clone the repo & cd:

```
git clone https://github.com/amine0110/Medical-Conversions
cd Medical-Conversions
```

2. Install the requirements.txt file:

```
pip install -r requirements.txt
```

3. Run the `main` script:

```
python main.py
```
-------------------------------------------------------------------------------------

And this is the window that you will get:

![image](https://user-images.githubusercontent.com/37108394/154864750-c55a3129-67c7-438a-8549-e2c45c433048.png)



- `Open File`: to open then convert one file only.
- `Open Dir`: to open then convert a directory which means multiple files at the same directory will be converted in one click.

-------------------------------------------------------------------------------------
## The main functions

Converting normal image into dicom file, which is explained in this [blog post](https://pycad.co/convert-jpg-or-png-images-into-dicom/).

```Python
def convert_image_to_dicom(in_dir, out_dir):
    ds = pydicom.dcmread('utils/dicom_sample.dcm') # pre-existing dicom file
    image = Image.open(in_dir) # the PNG or JPG file to be replace

    if image.mode == 'L':
        
        np_image = np.array(image.getdata(),dtype=np.uint8)
        ds.Rows = image.height
        ds.Columns = image.width
        ds.PhotometricInterpretation = "MONOCHROME1"
        ds.SamplesPerPixel = 1
        ds.BitsStored = 8
        ds.BitsAllocated = 8
        ds.HighBit = 7
        ds.PixelRepresentation = 0
        ds.PixelData = np_image.tobytes()
        ds.save_as(out_dir + '.dcm')

    elif image.mode == 'RGBA':

        np_image = np.array(image.getdata(), dtype=np.uint8)[:,:3]
        ds.Rows = image.height
        ds.Columns = image.width
        ds.PhotometricInterpretation = "RGB"
        ds.SamplesPerPixel = 3
        ds.BitsStored = 8
        ds.BitsAllocated = 8
        ds.HighBit = 7
        ds.PixelRepresentation = 0
        ds.PixelData = np_image.tobytes()
        ds.save_as(out_dir + '.dcm')
```

Converting dicom file into jpg image, as explained in this [blog post](https://pycad.co/how-to-convert-a-dicom-image-into-jpg-or-png/)

```Python
def convert_dcm_jpg(in_dir, out_dir):
    
    im = pydicom.dcmread(in_dir)

    im = im.pixel_array.astype(float)

    rescaled_image = (np.maximum(im,0)/im.max())*255 # float pixels
    final_image = np.uint8(rescaled_image) # integers pixels

    final_image = Image.fromarray(final_image)
    final_image.save(out_dir + '.jpg')
```

Converting nifti into dicom using SimpleITK, the idea came from [this function](https://simpleitk.readthedocs.io/en/next/Examples/DicomSeriesFromArray/Documentation.html) that converts an array into dicom series.

```Python
def convert_nifti_to_dicom(in_dir, out_dir):
    new_img = sitk.ReadImage(in_dir) 
    modification_time = time.strftime("%H%M%S")
    modification_date = time.strftime("%Y%m%d")

    direction = new_img.GetDirection()
    series_tag_values = [("0008|0031",modification_time), # Series Time
                    ("0008|0021",modification_date), # Series Date
                    ("0008|0008","DERIVED\\SECONDARY"), # Image Type
                    ("0020|000e", "1.2.826.0.1.3680043.2.1125."+modification_date+".1"+modification_time), # Series Instance UID
                    ("0020|0037", '\\'.join(map(str, (direction[0], direction[3], direction[6],# Image Orientation (Patient)
                                                        direction[1],direction[4],direction[7])))),
                    ("0008|103e", "Created-SimpleITK")] # Series Description

    # Write slices to output directory
    list(map(lambda i: writeSlices(series_tag_values, new_img, i, out_dir), range(new_img.GetDepth())))
```

Which depends to this function:

```Python
def writeSlices(series_tag_values, new_img, i, out_dir):
    image_slice = new_img[:,:,i]
    writer = sitk.ImageFileWriter()
    writer.KeepOriginalImageUIDOn()

    # Tags shared by the series.
    list(map(lambda tag_value: image_slice.SetMetaData(tag_value[0], tag_value[1]), series_tag_values))

    # Slice specific tags.
    image_slice.SetMetaData("0008|0012", time.strftime("%Y%m%d")) # Instance Creation Date
    image_slice.SetMetaData("0008|0013", time.strftime("%H%M%S")) # Instance Creation Time

    # Setting the type to CT preserves the slice location.
    image_slice.SetMetaData("0008|0060", "CT")  # set the type to CT so the thickness is carried over

    # (0020, 0032) image position patient determines the 3D spacing between slices.
    image_slice.SetMetaData("0020|0032", '\\'.join(map(str,new_img.TransformIndexToPhysicalPoint((0,0,i))))) # Image Position (Patient)
    image_slice.SetMetaData("0020,0013", str(i)) # Instance Number

    # Write to the output directory and add the extension dcm, to force writing in DICOM format.
    writer.SetFileName(os.path.join(out_dir,'slice' + str(i).zfill(4) + '.dcm'))
    writer.Execute(image_slice)
```

## 🆕 NEW

Full course about medical imaging segmentation is coming soon, join the waitlist here:

https://pycad.co/monai-and-pytoch-for-medical-imaging/
