from setuptools import setup

try:
    with open("./README.md", "r") as f:
        readme = f.read()
except Exception as e:
    readme = ""


setup(
    name='django-user-g11n',
    author="salexkidd",
    author_email="salexkidd@gmail.com",
    url="https://github.com/salexkidd/django-user-g11n",
    description='User g11n extension for Django',
    long_description_content_type="text/markdown",
    long_description=readme,
    keywords=["django", "i18n", "l10n", "g11n", "timezone", ],
    version='0.3',
    packages=['user_g11n'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
