from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='satlll',
    version="0.1.0",
    description='A Python tool that implements Lovasz Local Lemma\'s application on The Boolean Satisfiability (SAT) problem, which includes an instance geneartor,an algorithm (decision procedure), which decide that if a SAT instance satisfies in local lemma regime, and a solver can find solution or sample a uniform random solution in the local lemma regime.',
    author="wwen",
    author_email="wenwh96@gmail.com",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
    ],
    keywords='lovasz sat',
    url='https://github.com/opensat/PyLLL',
    packages=find_packages(exclude=['example', '.ipynb_checkpoints', '.vscode', 'backup', 'formulas', 'images', 'industrial_formulas', 'unsolve_formulas', 'phase_transition.ipynb']),
    python_requires='>=3.5',
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
