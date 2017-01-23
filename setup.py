from setuptools import setup, find_packages

setup(
    name='django-tinyuuidfield',
    version='0.1',
    author='Martin Simensen',
    author_email='simensen94@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/martsime/django-tinyuuidfield',
    license='BSD licence, see LICENCE file',
    description='Tiny UUIDField for Django. In case you want unique uuid for urls. Flexible length.',
    long_description='Tiny UUIDField for Django. In case you want unique uuid for urls. Flexible length.',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
