# S-Parameter to TDR Viewer
A S-Parameter to TDR Viewer using Scikit-rf  
  
Many Circuit Analysis, EM Solver programs and lower cost Network Anayzers can measure circuits, but can only produce S-Parameter files.  
With this program you can read and convert those S-Parameter files to a Time Domain Reflectrometry (TDR) view.  
  
# An Example:  
This circuit consisting of some different impedance transmission lines can be analyzed by a frequency domanin Circuit Analysis program,  
  
![images/S2P Test Network Figure.PNG](https://github.com/Hagtronics/S-Parameter-to-TDR-Viewer/blob/main/images/S2P%20Test%20Network%20Figure.PNG)  
  
To get the TDR view from the S-Parameter file - you can use the program presented here,  
  
![analysis](images/overview.jpg)  
  
See the 'User Guide' for a full walk through of the program.  
  
# Installing the program  
1) Get the code from the src directory.  
2) Use the 'requirements.txt' file to get the proper python libraries.  
3) Double Click on the file: 'sparam_to_tdr.py' to run the program.

# Acknowledgments 
Thanks to PyGuBu for making building TTKInter GUI's so easy. [PyGuBu](https://pypi.org/project/pygubu/)
Thanks to Scikit-rf for doing al the 'heavy lifting' computation here.  
Thanks always to Matplotlib for making graphics so painless.
