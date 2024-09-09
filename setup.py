from  setuptools import setup, find_packages

setup(
    name='django-auth-helper',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
        'djoser>=2.1.0',
        'djangorestframework>=3.12.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)