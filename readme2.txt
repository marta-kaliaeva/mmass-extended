The extended version of mmass includes the following new features/extensions:
1.	Changes in “Adduct” column appearing in “Compound Search” panel. Format changed, now displaying for example [M+H]+ or [M+Na]+, instead of empty value for hydrogen adduct or Na+.

2.	Added new buttons to panel “Compound Search” for correct annotations of ¹³C and ¹⁵N isotope variant or its combination, which might be useful for metabolomics studies where annotation of particular isotope is required.

3.	New column “Isotope” added to panel “Compound Search”. Selected isotopes of ¹³C or ¹⁵N (or both) are displayed in this panel.

4.	Changes in “m/z” column in “Compound Search” panel. Column renamed to “m/z database”, as the mass of the compound displayed here is theoretical value computed from formula in database (Libraries/Compounds).

5.	New column “m/z measured” added to panel “Compound Search”. After matching peak m/z, mass error in ppm is given and real peak m/z value appears in this column.

6.	New ion/adduct variants added. In negative mode we added [M-CH3]-, [M-C3H10N]- and [M-C5H12N]- ions which might be relevant under certain conditions for (lyso)phosphatidylcholines and (lyso)phosphatidic acids. We also added 2M type ions, both in positive and negative mode. Next, we added main ions after derivatization with FMP-10 matrix and AMPP derivatization.

7.	We added “Cubic” calibration method to panel “Calibrations”.

8.	We grabbed publicly available HMDB v5 database and added it into “Libraries/Compounds”. The whole database is large so we split it according to provider’s annotations into four main parts: Quantified, Detected, Expected and Predicted. We made combination of Quantified and Detected which we think might be useful. 

9.	Minor formatting changes, such as adjusting decimal places, table sizes, column sizes, and text formatting.

10.	The sorting system in the “Compound Search” panel has been improved so that compounds can be sorted by m/z values in ascending or descending order. Sorting by compound name in alphabetical order is also possible.


***The extended version of mmass v.2 includes the following new features/extensions***:
***Download the archive mmass - extended v.2, and replace the gui and mspy folders in the previous version with the new ones from the archive.***

1. Isotopes ¹³C and ¹⁵N, as well as their combinations, have been added to the annotations. In the previous version, only the adduct could be seen. 
Additionally, the font used for isotopes and their combinations in the annotations has been changed, and superscripts and subscripts have been added for clearer representation.

2. It is also possible to change the font size and toolbar size. Here's how you can do it, if needed, depending on your screen size: 
 1) To change the font size for documents (annotations), go to panel_documents.py (GUI) and find this part of the code: # $$ 15.05.2025 Unicode symbols fix annotation
    font = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Segoe UI Symbol")
 2) To change the font size for interface font, go to mwx.py (GUI) and find this part of the code:
    # GUI CONSTANTS
    # -------------
    SMALL_FONT_SIZE = 11 #$$8
    NORMAL_FONT_SIZE = 12 #$$9
 3) To change the size of the top (toolbar) icons, go to images.py  (GUI) and look for this part of the code:
    # $$ all rows with scaleBitmap(tools...)
        toolsBitmapSize = (30, 30)
 4) To change the size of the bottom (toolbar) icons, go to images.py  (GUI) and look for this part of the code:
     # $$ all rows with scaleBitmap(bottombarsOn/Off...)+ go to mvx.py and change height
     bottombarBitmapSize = (36, 27)
     Go to mwx.py (GUI) and look for this part of the code:
     # $$ must match the bottombarBitmapSize's height in images.py
     BOTTOMBAR_HEIGHT = 27
