# Model Repository

This repository contains the code and resources for the model used in the competition. To ensure the model runs properly, you need to download and extract the model weights.

## Downloading and Extracting Model Weights

The model weights are provided as a zip file hosted on Google Drive. Follow the steps below to download and extract them into the `weights` directory.

### Step 1: Create Weights Directory

First, create a directory named `weights` if it doesn't already exist:

mkdir -p weights

### Step 2: Download the Weights Zip File

Use the following code block to download the zip file containing the model weights. **Remember to replace the placeholder `FILE_ID` with your actual Google Drive file ID.**

FILE_ID="1FbwQvZH3afAqRArHlQP72pP9Cf7HGNfK"
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?id=$FILE_ID&export=download' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$FILE_ID" -O weights.zip && rm -rf /tmp/cookies.txt


### Step 3: Extract the Weights
After downloading, extract the contents of the zip file into the `weights` directory

unzip weights.zip -d weights


### Step 4: Clean Up

Optionally, you can remove the zip file after extraction to save space:

rm weights.zip





## Important Notes

- **Dependencies**: Ensure you have `wget` and `unzip` installed on your system. You can install them using:
  - For Debian/Ubuntu:
    ```
    sudo apt-get install wget unzip
    ```
  - For macOS (using Homebrew):
    ```
    brew install wget unzip
    ```
  
- **Google Drive Permissions**: Make sure that your Google Drive file is set to allow access for anyone with the link.
  
- **File ID**: Ensure you replace the `FILE_ID` in the script with your actual Google Drive file ID.

## Conclusion

Following these steps will ensure that you have all necessary files downloaded and extracted correctly. If you have any questions or need further assistance, feel free to reach out!

