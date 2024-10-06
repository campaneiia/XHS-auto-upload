# XHS Posting Automation Tool

This tool automates the process of uploading content to Xiaohongshu (Little Red Book). Follow the setup instructions below to get started.

## Setup Instructions

### Prerequisites

Ensure you have the following before proceeding:
- Python 3.11.1  
- Download WebDriver provided by Firefox
>  [geckodriver](https://github.com/mozilla/geckodriver)


### Clone the Project

Clone the repository to your local machine using the following command:

```shell
git clone https://github.com/campaneiia/XHS-auto-upload.git
```

### Navigating to the Project Folder

Change your directory to the cloned project folder:

```shell
cd xiaohongshu
```

### Setting Up the Virtual Environment

Create a virtual environment to manage dependencies:

```shell
python -m venv venv
```

### Activate the Virtual Environment

```shell
.\venv\Scripts\activate
```

### Installing Dependencies

Install the required Python packages from ```requirements.txt```:

```shell
pip install -r requirements.txt
```

## Script Instructions

### How to Run the Script

Execute the following command in your shell:
```shell
python main.py
```

### Login Process

- Cookie Check: Initially, the script checks if the ```Cookie``` in ```cookies.json``` is valid. If ```Cookie``` is invalid or the file is absent, you will need to log in by using your phone number to receive a verification code. By default, the script uses the ```Cookie``` for login when available.
- Cookie Storage: Upon successful login, ```Cookie``` will be saved in ```cookies.json``` 

### General Features

- Exiting the Script: Use ```ctrl + c``` to exit the script at any time.  
- Navigation: Enter ```back``` to go back to the previous menu.


### Uploading Videos

- Video Path: Provide the full path to the video file you wish to upload.
- Cover Upload (Optional): Xiaohongshu automatically generates a video cover using its first frame. However, you can upload a custom cover to enhance appeal.

> Supported video formats: ```.mp4```, ```.mov```, ```.flv```, ```.f4v```, ```.mkv```, ```.rm```, ```.rmvb```, ```.m4v```, ```.mpg```, ```.mpeg```, ```.ts```.


### Uploading Images

- Image Path File: Provide the path to a ```txt``` file containing the path of the image(s) you wish to upload.

- Quantity: You can upload a minimum of 1 and a maximum of 9 images per post. Use ```Enter```(aka New Line) to separate paths when uploading multiple images.

> Supported image formats: ```.jpg```, ```.jpeg```, ```.png```, ```.webp```.


### Uploading Title, Content, and Tags (For Both Video and Images)

- Title: First, you'll be prompted to enter the title of your post.
- Content: Then, upload the content by providing the path to its ```txt``` file.
- Tags (Optional): Finally, add tags to your post if desired. Start each tag with ```#``` and separate multiple tags with spaces.

