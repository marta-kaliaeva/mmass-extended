import sys
from gui.config import version, nightbuild

# make version label
if nightbuild:
    version = '%s (%s)' % (version, nightbuild)

# make win32 distribution using PyInstaller
if sys.platform == 'win32':
    from PyInstaller.__main__ import run  # Import PyInstaller for Windows
    
    # list additional files
    additionalFiles = [
        ("configs", [
            "configs/monomers.xml",
            "configs/compounds.xml",
            "configs/config.xml",
            "configs/enzymes.xml",
            "configs/mascot.xml",
            "configs/modifications.xml",
            "configs/presets.xml",
            "configs/references.xml",
        ]),
        ("", [
            "license.txt",
            "readme.txt",
            "User Guide.pdf",
        ]),
    ]
    
    # Build the executable using PyInstaller
    options = [
        'mmass.py',  # Replace with your actual script file
        '--onefile',  # Create a single executable
        '--add-data', 'configs/*;configs',  # Include the configs folder
        '--add-data', 'license.txt;.',  # Include the license file
        '--add-data', 'readme.txt;.',  # Include the readme file
        '--add-data', 'User Guide.pdf;.',  # Include the user guide
        '--icon=gui/images/msw/icon.ico',  # Set the application icon
    ]
    run(options)  # Run the PyInstaller command with the specified options


# make OSX distribution using py2app (unchanged from your original code)
if sys.platform == 'darwin':
    from setuptools import setup
    import py2app
    
    # list additional files for macOS
    additionalFiles = [
        "gui/images/mac/icon_doc_msd.icns",
        "gui/images/mac/icon_doc_mzdata.icns",
        "gui/images/mac/icon_doc_mzxml.icns",
        "gui/images/mac/icon_doc_mzml.icns",
        "gui/images/mac/icon_doc_fid.icns",
        "configs",
        "User Guide.pdf"
    ]
    
    # py2app options for macOS
    py2appOptions = dict(
        iconfile='gui/images/mac/icon.icns',
        argv_emulation=1,
        compressed=1,
        optimize=1,
        plist=dict(
            CFBundleName="mMass",
            CFBundleDisplayName="mMass",
            CFBundleExecutable="mMass",
            CFBundleSignature="mMass",
            CFBundleIdentifier="org.mmass",
            CFBundlePackageType="APPL",
            CFBundleShortVersionString=version,
            CFBundleVersion=version,
            CFBundleGetInfoString="mMass - Open Source Mass Spectrometry Tool",
            CFBundleIconFile="icon.icns",
            NSHumanReadableCopyright="(c) 2005-2013 Martin Strohalm",
            LSHasLocalizedDisplayName=False,
            NSAppleScriptEnabled=False,
            CFBundleDocumentTypes=[
                dict(
                    CFBundleTypeExtensions=["msd"],
                    CFBundleTypeName="mMass Spectrum Document",
                    CFBundleTypeIconFile="icon_doc_msd.icns",
                    CFBundleTypeOSTypes=["TEXT"],
                    CFBundleTypeRole="Editor",
                    NSDocumentClass="MyDocument",
                ),
                dict(
                    CFBundleTypeExtensions=["mzdata"],
                    CFBundleTypeName="mzData Mass Spectrum Document",
                    CFBundleTypeIconFile="icon_doc_mzdata.icns",
                    CFBundleTypeOSTypes=["TEXT"],
                    CFBundleTypeRole="Viewer",
                    NSDocumentClass="MyDocument",
                ),
                dict(
                    CFBundleTypeExtensions=["mzxml"],
                    CFBundleTypeName="mzXML Mass Spectrum Document",
                    CFBundleTypeIconFile="icon_doc_mzxml.icns",
                    CFBundleTypeOSTypes=["TEXT"],
                    CFBundleTypeRole="Viewer",
                    NSDocumentClass="MyDocument",
                ),
                dict(
                    CFBundleTypeExtensions=["mzml"],
                    CFBundleTypeName="mzML Mass Spectrum Document",
                    CFBundleTypeIconFile="icon_doc_mzml.icns",
                    CFBundleTypeOSTypes=["TEXT"],
                    CFBundleTypeRole="Viewer",
                    NSDocumentClass="MyDocument",
                ),
                dict(
                    CFBundleTypeExtensions=["mgf"],
                    CFBundleTypeName="Mascot Generic Format",
                    CFBundleTypeIconFile="icon_doc_mgf.icns",
                    CFBundleTypeOSTypes=["TEXT"],
                    CFBundleTypeRole="Viewer",
                    NSDocumentClass="MyDocument",
                ),
            ],
        ),
    )
    
    # main setup for macOS
    setup(
        app=['mmass.py'],
        setup_requires=["py2app"],
        name="mMass",
        author="Martin Strohalm",
        url='http://www.mmass.org/',
        license='GNU General Public License',
        options=dict(py2app=py2appOptions),
        data_files=additionalFiles
    )