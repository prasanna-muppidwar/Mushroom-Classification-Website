# Mushroom-Classification 

This repository contains a machine learning model trained to classify mushrooms as edible or poisonous based on certain features. The model is implemented using a decision tree algorithm.

<div align="center">
  <img src="https://github.com/prasanna-muppidwar/Mushroom-Classification/blob/main/Mushroom-Classification-master/Mushroom%20Classification.png" alt="Mushroom Classification" style="max-width: 100%; height: auto;">
</div>

# Dataset
The dataset used for training and testing the model consists of samples of mushrooms, where each sample is characterized by the following input features:
- Gill Size
- Gill Color
- Stalk Root
- Spore Print Color
- Population

The target variable is the classification of the mushroom as either **"edible"** or **"poisonous"**.

Link: https://www.kaggle.com/datasets/uciml/mushroom-classification

# Model

The decision tree algorithm was chosen for this classification task.


# Usage
To use this project, follow these steps:

1. Run <code>pip install virtualenv </code>
2. Create a python Virtual environment:
<code>virtualenv envname</code>
3. To activate the environment:<br>
a: <code>cd envname</code><br>
b: <code>Scripts\activate</code>
4. Move back to Main directory:
<code>cd ..</code>
5. Install required libraries:
<code>pip install -r requirements.txt</code>
6. Run the app:
<code>python app.py</code>



