from setuptools import setup, find_packages

def read_requirements(path:str='requirements.txt'):
    requirements = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line == '-e .':
                continue
            requirements.append(line)

    return requirements

setup(
    name="V1_app",
    version="0.0.1",
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    description="A sample python application",
    author="Sameer Khan",
    author_email="sameerkhanofficial2401@gmail.com",
    url="https://github.com/samkhan0007/ML_Project/tree/main",
)