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

The model weights are provided as a zip file hosted on Google Drive. Follow the steps below to download and extract them.

### Step 1: Download the Weights Zip File

Use the following code block to download the zip file containing the model weights from the provided Google Drive link:

```bash
gdown --id 1IrFc3PhIKDx2hJPATrALEUbeZeeWDcuR -O weights.zip
```

### Step 2: Extract the Weights

After downloading, extract the contents of the zip file:

```bash
# For Linux/Mac
unzip weights.zip -d weights

# For Windows
# Use File Explorer to extract the zip file into the weights folder
# Or use a tool like 7-Zip or WinRAR
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

- **Dependencies**: 
  - Python 3.7 or higher
  - gdown: Install with `pip install gdown`
  - For Linux/Mac: Ensure you have `unzip` installed
  - For Windows: Use built-in extraction tools or install 7-Zip
  
- **Google Drive Permissions**: Make sure that the Google Drive file is accessible. The link should be set to "Anyone with the link can view."
  
- **Alternative Download Method**: If you encounter issues with gdown, you can manually download the file from the Google Drive link and move it to the weights directory.

## Conclusion

Following these steps will ensure that you have all necessary files downloaded and extracted correctly. If you have any questions or need further assistance, feel free to reach out!