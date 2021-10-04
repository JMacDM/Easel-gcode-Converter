Easily Convert your Easel designs into gcode you can use on your 3d printer with laser attached to parts cooling fan port (M106 in gcode)
allows 5 shades which you set by the depth of cut in Easel.
Python script will then convert z movements to laser intensities, and generate a gcode file from the Easel .nc file.
Will add support for alternate Smoothieboard mosfets soon
Will add support for grbl laser control if there is interest.

//// Be sure to read Setup and Use before using.\\\\


/////////////////////// Setup:\\\\\\\\\\\\\\\\\\\\\\

1) Make sure units are set to mm in bottom left corner.
2) In General Settings menu, set Safety Height to 2mm, and Origin Safety Height to 0mm. Menu is in Machine tab on top of page.
3) Set Material Dimensions Thickness(Z) 2.5mm. Other dimensions should be close to the size of the workarea.
4) Create "Other" bit with around 0.5mm width. May vary depending on laser precision and power.
5) Under Cut Settings select Manual and set Feed rate to 300mm/min, Plunge 150mm/min, Depth per pass to 2.5

//////////////////////// Use:\\\\\\\\\\\\\\\\\\\\\\\\\

Place items as you usually would, but make cuts in increments of .5mm. 
2.5mm cut is 100% laser
2.0mm cut is 80%
1.5mm cut is 60%
1.0mm cut is 40%
.5mm cut is 20%
Download gcode from Easel.
Place gcode in directory with the folder containing script. (directory above script)
when prompted type in easel file name without .nc extension
file will be placed in folder with original file.

