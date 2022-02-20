from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from functions import convert_image_to_dicom, convert_dcm_jpg, convert_nifti_to_dicom
from glob import glob
import dicom2nifti
import os

def progress_bar(master):
    progress_bar = Progressbar(master, mode='determinate', orient='horizontal', length=500)
    progress_bar.pack(pady=(20,0))

    return progress_bar

def call_home_page():
    root.geometry('700x500')
    home_page = Frame(root, bg=bg)
    home_page.grid(row=0, column=0, sticky='nsew')

    title = Label(home_page, text='Medical Conversions', bg=bg, fg='#ffffff', font='Arial 35 bold')
    title.pack(pady=(20,0))

    buttons_frame = Frame(home_page, bg=bg)
    buttons_frame.pack(pady=(50,0))

    image_to_dicom_button = Button(buttons_frame, text='Image\nto\nDicom', font='none 20 bold', width=10, fg='#053047', command=image_to_dicom_page)
    image_to_dicom_button.grid(row=0, column=0)

    dicom_to_image_button = Button(buttons_frame, text='Dicom\nto\nImage', font='none 20 bold', width=10, fg='#053047', command=dicom_to_image_page)
    dicom_to_image_button.grid(row=0, column=1, padx=(50,0))

    dicom_to_nifti_button = Button(buttons_frame, text='Dicom\nto\nNifti', font='none 20 bold', width=10, fg='#053047', command=dicom_to_nifti_page)
    dicom_to_nifti_button.grid(row=1, column=0, pady=(50,0))

    nifti_to_dicom_button = Button(buttons_frame, text='Nifti\nto\nDicom', font='none 20 bold', width=10, fg='#053047', command=nifti_to_dicom_page)
    nifti_to_dicom_button.grid(row=1, column=1, padx=(50,0), pady=(50,0))

def image_to_dicom_page():
    global text_message_i_d
    root.geometry('600x450')
    image_to_dicom = Frame(root, bg=bg)
    image_to_dicom.grid(row=0, column=0, sticky='nsew')

    title = Label(image_to_dicom, text='Image to Dicom', bg=bg, fg='#ffffff', font='Arial 35 bold')
    title.pack()

    open_buttons = Frame(image_to_dicom, bg=bg)
    open_buttons.pack(pady=(30,0))

    open_file = Button(open_buttons, text='Open File', font='none 20 bold', width=10, fg='#053047', command=call_open_file_image_to_dicom)
    open_file.grid(row=0, column=0, padx=(0,20))

    open_dir = Button(open_buttons, text='Open Dir', font='none 20 bold', width=10, fg='#053047', command=call_open_dir_image_to_dicom)
    open_dir.grid(row=0, column=1, padx=(20,0))

    convert_save = Button(image_to_dicom, text='Convert & Save', font='none 20 bold', fg='#053047', command=call_convert_save_image_to_dicom)
    convert_save.pack(pady=(40,0))

    text_message_i_d = Label(image_to_dicom,text='Choose file or dir', font='none 9', bg=bg, fg='#FFFFFF')
    text_message_i_d.pack(pady=(20,0))

    home_button = Button(image_to_dicom, text='Home', command=call_home_page, font='none 13 bold', width=10, fg='#053047')
    home_button.pack(pady=(40,20))

def dicom_to_image_page():
    global dicom_to_image
    global text_message_d_i

    root.geometry('600x450')
    dicom_to_image = Frame(root, bg=bg)
    dicom_to_image.grid(row=0, column=0, sticky='nsew')

    title = Label(dicom_to_image, text='Dicom to Image', bg=bg, fg='#ffffff', font='Arial 35 bold')
    title.pack()

    open_buttons = Frame(dicom_to_image, bg=bg)
    open_buttons.pack(pady=(30,0))

    open_file = Button(open_buttons, text='Open File', font='none 20 bold', width=10, fg='#053047', command=call_open_file_dicom_to_image)
    open_file.grid(row=0, column=0, padx=(0,20))

    open_dir = Button(open_buttons, text='Open Dir', font='none 20 bold', width=10, fg='#053047', command=call_open_dir_dicom_to_image)
    open_dir.grid(row=0, column=1, padx=(20,0))

    convert_save = Button(dicom_to_image, text='Convert & Save', font='none 20 bold', fg='#053047', command=call_convert_save_dicom_to_image)
    convert_save.pack(pady=(40,0))

    text_message_d_i = Label(dicom_to_image,text='Choose file or dir', font='none 9', bg=bg, fg='#FFFFFF')
    text_message_d_i.pack(pady=(20,0))

    home_button = Button(dicom_to_image, text='Home', command=call_home_page, font='none 13 bold', width=10, fg='#053047')
    home_button.pack(pady=(40,20))

def dicom_to_nifti_page():
    global text_message_d_n
    root.geometry('600x450')
    dicom_to_nifti = Frame(root, bg=bg)
    dicom_to_nifti.grid(row=0, column=0, sticky='nsew')

    title = Label(dicom_to_nifti, text='Dicom to Nifti', bg=bg, fg='#ffffff', font='Arial 35 bold')
    title.pack()

    open_buttons = Frame(dicom_to_nifti, bg=bg)
    open_buttons.pack(pady=(30,0))

    open_file = Button(open_buttons, text='Open Dir', font='none 20 bold', width=10, fg='#053047', command=call_open_file_dicom_to_nifti)
    open_file.grid(row=0, column=0, padx=(0,20))

    open_dir = Button(open_buttons, text='Open Dirs', font='none 20 bold', width=10, fg='#053047', command=call_open_dir_dicom_to_nifti)
    open_dir.grid(row=0, column=1, padx=(20,0))

    convert_save = Button(dicom_to_nifti, text='Convert & Save', font='none 20 bold', fg='#053047', command=call_convert_save_dicom_to_nifti)
    convert_save.pack(pady=(40,0))

    text_message_d_n = Label(dicom_to_nifti,text='Choose file or dir', font='none 9', bg=bg, fg='#FFFFFF')
    text_message_d_n.pack(pady=(20,0))

    home_button = Button(dicom_to_nifti, text='Home', command=call_home_page, font='none 13 bold', width=10, fg='#053047')
    home_button.pack(pady=(40,20))

def nifti_to_dicom_page():
    global text_message_n_d
    root.geometry('600x450')
    nifti_to_dicom = Frame(root, bg=bg)
    nifti_to_dicom.grid(row=0, column=0, sticky='nsew')

    title = Label(nifti_to_dicom, text='Nifti to Dicom', bg=bg, fg='#ffffff', font='Arial 35 bold')
    title.pack()

    open_buttons = Frame(nifti_to_dicom, bg=bg)
    open_buttons.pack(pady=(30,0))

    open_file = Button(open_buttons, text='Open File', font='none 20 bold', width=10, fg='#053047', command=call_open_file_nifti_dicom)
    open_file.grid(row=0, column=0, padx=(0,20))

    open_dir = Button(open_buttons, text='Open Dir', font='none 20 bold', width=10, fg='#053047', command=call_open_dir_nifti_to_dicom)
    open_dir.grid(row=0, column=1, padx=(20,0))

    convert_save = Button(nifti_to_dicom, text='Convert & Save', font='none 20 bold', fg='#053047', command=call_convert_save_nifti_to_dicom)
    convert_save.pack(pady=(40,0))

    text_message_n_d = Label(nifti_to_dicom,text='Choose file or dir', font='none 9', bg=bg, fg='#FFFFFF')
    text_message_n_d.pack(pady=(20,0))

    home_button = Button(nifti_to_dicom, text='Home', command=call_home_page, font='none 13 bold', width=10, fg='#053047')
    home_button.pack(pady=(40,20))

def call_open_file_image_to_dicom():
    global flag_image_dicom
    global in_path_image_dicom
    global text_message_i_d
    
    
    in_path_image_dicom = filedialog.askopenfile()
    if in_path_image_dicom: 
        flag_image_dicom = 1
        text_message_i_d.config(text='You opened: \n' + in_path_image_dicom.name)

def call_open_dir_image_to_dicom():
    global flag_image_dicom
    global in_path_image_dicom
    global text_message_i_d
    
    in_path_image_dicom = filedialog.askdirectory()
    if in_path_image_dicom:
        flag_image_dicom = 2
        text_message_i_d.config(text='You opened: \n' + in_path_image_dicom)

def call_convert_save_image_to_dicom():
    global text_message_i_d
    if flag_image_dicom == 1 and in_path_image_dicom:
        out_path = filedialog.asksaveasfilename()
        if out_path:
            convert_image_to_dicom(in_path_image_dicom.name, out_path)
            text_message_i_d.config(text='File saved at\n' + out_path + '.dcm')
    
    if flag_image_dicom == 2 and in_path_image_dicom:
        
        images = glob(in_path_image_dicom + '/*')
        out_path = filedialog.askdirectory()
        if out_path:
            for i, image in enumerate(images):
                
                convert_image_to_dicom(image, out_path + '/file' + str(i).zfill(len(str(len(images)))))
                text_message_i_d.config(text='Files saved at\n' + out_path)
                
def call_open_file_dicom_to_image():
    global flag_dicom_image
    global in_path_dicom_image
    global text_message_d_i
   
    in_path_dicom_image = filedialog.askopenfile()
    if in_path_dicom_image:
        flag_dicom_image = 1
        text_message_d_i.config(text='You opened: \n' + in_path_dicom_image.name)

def call_open_dir_dicom_to_image():
    global flag_dicom_image
    global in_path_dicom_image
    global text_message_d_i

    in_path_dicom_image = filedialog.askdirectory()

    if in_path_dicom_image:
        flag_dicom_image = 2
        text_message_d_i.config(text='You opened: \n' + in_path_dicom_image)

def call_convert_save_dicom_to_image():
    global text_message_d_i

    if flag_dicom_image == 1 and in_path_dicom_image:
        out_path = filedialog.asksaveasfilename()
        if out_path:
            convert_dcm_jpg(in_path_dicom_image.name, out_dir=out_path)
            text_message_d_i.config(text='File saved at\n' + out_path + '.dcm')

    if flag_dicom_image == 2 and in_path_dicom_image:
        
        images = glob(in_path_dicom_image + '/*.dcm')
        out_path = filedialog.askdirectory()
        if out_path:
            for i, image in enumerate(images):
                convert_dcm_jpg(image, out_path + '/image' + str(i).zfill(len(str(len(images)))))
                text_message_d_i.config(text='Files saved at\n' + out_path)
                
def call_open_file_dicom_to_nifti():
    global flag_dicom_nifti
    global in_path_dicom_nifti
    global text_message_d_n
    
    
    in_path_dicom_nifti = filedialog.askdirectory()
    if in_path_dicom_nifti: 
        flag_dicom_nifti = 1
        text_message_d_n.config(text='You opened: \n' + in_path_dicom_nifti)

def call_open_dir_dicom_to_nifti():
    global flag_dicom_nifti
    global in_path_dicom_nifti
    global text_message_d_n

    in_path_dicom_nifti = filedialog.askdirectory()

    if in_path_dicom_nifti:
        flag_dicom_nifti = 2
        text_message_d_n.config(text='You opened: \n' + in_path_dicom_nifti)

def call_convert_save_dicom_to_nifti():
    global text_message_d_n
    text_message_d_n.config(text='Converting...')

    if flag_dicom_nifti == 1 and in_path_dicom_nifti:
        out_path = filedialog.asksaveasfilename()
        if out_path:
            dicom2nifti.dicom_series_to_nifti(in_path_dicom_nifti, out_path + '.nii.gz')
            text_message_d_n.config(text='File saved at\n' + out_path + '.nii.gz')

    if flag_dicom_nifti == 2 and in_path_dicom_nifti:
        images = glob(in_path_dicom_nifti + '/*')
        out_path = filedialog.askdirectory()
        if out_path:
            for i, image in enumerate(images):
                text_message_d_n.config(text='Converting...')
                dicom2nifti.dicom_series_to_nifti(image, out_path + '/' + os.path.basename(image) + str(i).zfill(len(str(len(images)))) + '.nii.gz')
                text_message_d_n.config(text='Files saved at\n' + out_path)

def call_open_file_nifti_dicom():
    global flag_nifti_dicom
    global in_path_nifti_dicom
    global text_message_n_d
    
    
    in_path_nifti_dicom = filedialog.askopenfilename()
    if in_path_nifti_dicom: 
        flag_nifti_dicom = 1
        text_message_n_d.config(text='You opened: \n' + in_path_nifti_dicom)

def call_open_dir_nifti_to_dicom():
    global flag_nifti_dicom
    global in_path_nifti_dicom
    global text_message_n_d

    in_path_nifti_dicom = filedialog.askdirectory()

    if in_path_nifti_dicom:
        flag_nifti_dicom = 2
        text_message_n_d.config(text='You opened: \n' + in_path_nifti_dicom)

def call_convert_save_nifti_to_dicom():
    global text_message_n_d
    text_message_n_d.config(text='Converting...')

    if flag_nifti_dicom == 1 and in_path_nifti_dicom:
        out_path = filedialog.askdirectory()
        if out_path:
            convert_nifti_to_dicom(in_path_nifti_dicom, out_path)
            text_message_n_d.config(text='File saved at\n' + out_path + '.nii.gz')

    if flag_nifti_dicom == 2 and in_path_nifti_dicom:
        images = glob(in_path_nifti_dicom + '/*')
        out_path = filedialog.askdirectory()
        if out_path:
            for i, image in enumerate(images):
                text_message_n_d.config(text='Converting...')
                o_path = out_path + '/' + os.path.basename(image)[:-7]
                if not os.path.exists(o_path): os.makedirs(o_path)

                convert_nifti_to_dicom(image, o_path)
                text_message_n_d.config(text='Files saved at\n' + out_path)


##############################################################################
########################## This is the main function #########################
##############################################################################

if __name__ == '__main__':
    global in_path_image_dicom
    global in_path_dicom_image
    global in_path_nifti_dicom
    global in_path_dicom_nifti

    global flag_image_dicom
    global flag_dicom_image 
    global flag_nifti_dicom 
    global flag_dicom_nifti

    flag_image_dicom = 0
    flag_dicom_image = 0
    flag_nifti_dicom = 0
    flag_dicom_nifti = 0

    bg = '#053047'
    root = Tk()
    root.geometry('700x500')
    root.title('Pycad Convert')
    root.iconbitmap('utils/logo.ico')

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    call_home_page()

    root.mainloop()
    
