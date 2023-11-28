import os
from pathlib import Path

package_name = "Diamond_Price_Prediction"

# Names of folders and files to be created..
list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{package_name}/__init__.py",

    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",

    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",


    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/utils.py",

    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",

    "notebooks/data/.gitkeep",

    "notebooks/eda.ipynb",
    "notebooks/research.ipynb",
    "notebooks/model_training.ipynb",

    "requirements.txt",
    "setup.py",
    "init_setup.sh"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # If filedir string is non empty.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

    else:
        print("File already exist!!!")

