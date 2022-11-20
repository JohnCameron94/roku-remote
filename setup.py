import setuptools as stls
# Application Name
APP_NAME = 'RokuRemote'
# Main File to run
APP= ['app/app.py']
# App Meta
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app/view/icons/Application.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Roku Remote application",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2015, Johnahton Cameron, All Rights Reserved"
    }
}
# Setup
stls.setup(
    name=APP_NAME,
    version='0.0.1',
    url='',
    app=APP,
    author='Johnathon Cameron',
    author_email='johncam1994@gmail.com',
    description='Stand Alone Application, Roku Remote',
    install_requires=['py2app', 'requests',],
    packages=stls.find_packages(exclude=['config.ini','pytest.ini','tests', 'tests.*']),
    package_data={'': ['app/view/icons/*.png']},
    include_package_data=True,
    #options={'py2pp':{OPTIONS}}
    
)