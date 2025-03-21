# Model Repository

This repository contains the code and resources for the model used in the competition. To ensure the model runs properly, you need to download and extract the model weights.

## Cloning the Repository

Before getting started, you'll need to clone this repository to your local machine:

```bash
git clone https://github.com/quantmask/CV_SVNIT.git
cd CV_SVNIT
```

This will create a local copy of the repository and navigate to the project directory.

## Downloading and Extracting Model Weights

The model weights are provided as a zip file hosted on Google Drive. Follow the steps below to download and extract them into the `weights` directory.

### Step 1: Create Weights Directory

First, create a directory named `weights` if it doesn't already exist:

```bash
mkdir -p weights
```

### Step 2: Download the Weights Zip File

Use the following code block to download the zip file containing the model weights from the provided Google Drive link:

```bash
# Extract the file ID from the Google Drive link
FILE_ID="1FbwQvZH3afAqRArHlQP72pP9Cf7HGNfK"

# For files larger than 100MB (handles Google Drive download confirmation)
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?id=${FILE_ID}&export=download' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=${FILE_ID}" -O weights.zip && rm -rf /tmp/cookies.txt

# Alternative method for smaller files (if the above doesn't work)
# wget --no-check-certificate "https://docs.google.com/uc?export=download&id=${FILE_ID}" -O weights.zip
```

### Step 3: Extract the Weights

After downloading, extract the contents of the zip file into the `weights` directory:

```bash
unzip weights.zip -d weights
```

### Step 4: Clean Up

Optionally, you can remove the zip file after extraction to save space:

```bash
rm weights.zip
```

## Running the Model

After setting up the repository and downloading the weights, you can run the model using the test script:

```bash
# Linux/Mac
python ./test.py

# Windows Command Prompt
python test.py

# Windows PowerShell
python .\test.py
```

The test script will use the model weights from the `weights` directory to process the test data. Make sure you're in the repository's root directory when running this command.

## Important Notes

- **Dependencies**: Ensure you have `wget` and `unzip` installed on your system. You can install them using:
  - For Debian/Ubuntu:
    ```bash
    sudo apt-get install wget unzip
    ```
  - For macOS (using Homebrew):
    ```bash
    brew install wget unzip
    ```
  
- **Google Drive Permissions**: Make sure that the Google Drive file is accessible. The link should be set to "Anyone with the link can view."
  
- **Alternative Download Methods**: If you encounter issues with the wget command, you can also manually download the file from the link [https://drive.google.com/file/d/1FbwQvZH3afAqRArHlQP72pP9Cf7HGNfK/view?usp=sharing](https://drive.google.com/file/d/1FbwQvZH3afAqRArHlQP72pP9Cf7HGNfK/view?usp=sharing) and move it to the weights directory.

## Conclusion

Following these steps will ensure that you have all necessary files downloaded and extracted correctly. If you have any questions or need further assistance, feel free to reach out!