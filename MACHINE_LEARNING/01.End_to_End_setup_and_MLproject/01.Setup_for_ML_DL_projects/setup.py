from setuptools import find_packages, setup
from typing import List

Hypen_e_dot = '-e .'


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.replace("\n", "") for req in file_obj.readlines()]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

            return requirements


setup(name="Pkg_Diamond_price_prediction",
      version="0.0.1",
      author="rashmi_kumari",
      author_email="rashmikumari1504@gmail.com",
      install_requires=get_requirements('requirements.txt'),
      packages=find_packages()
      )

# Mention ackages from requirements.txt so that while being a locak package,
# # this local package will also able to use them.
