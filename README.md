# Aggression-Detection

***WARNING: The data, lexicons, and notebooks all contain content that is racist, sexist, homophobic, and offensive in many other ways.***

### Steps to run 

#### 1. Clone the repository
```
git clone https://www.github.com/Sandhya-G/Aggression-Detection.git
```

#### 2. Create virtual environment
On Linux 
```
python3 -m venv <environment_name>
```
activate the environment
```
source <environment_name>/bin/activate
```
 
On Windows
```
py -m venv <environment_name>
```
activate the environment
```
.\<environment_name>\Scripts\activate

```

#### 3. Install the dependencies
```
pip install -r requirements.txt
```

#### 4. Create a `glove` folder in your project directory.

#### 5. Download the Pretained Glove Embeddings from [here](https://www.kaggle.com/jdpaletto/glove-global-vectors-for-word-representation). 

#### 6.  Unzip the files and add them to the `glove` folder.

#### 7. Run the app
```
Flask run
```
