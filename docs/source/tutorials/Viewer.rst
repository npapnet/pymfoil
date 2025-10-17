Viewer (``tk_dic_viewer``)    
==========================


This is file that contains documentation foe the ``tk_dic_viewer`` tool.

.. image:: /tutorials/viewer_images/dic_viewer_gui.png  
   :alt: Dic Viewer Gui
   :width: 80%
   :height: 300px
   :scale: 50%
   :class: shadow

Some of the features of this tool are:

* It is a tkinter based GUI for producing offline graphs for the results of the DIC analysis (grid, markers, strain maps, displacement maps, etc.).
* the user needs to have already run the ``tk_dic_analysis`` tool to produce results.


Scope
-----

The aim of the tool is to reduce the size of the results and allow the user to view and accesss the results when he feels like it. I.e. the idea is to
keep the directory structure containing the camera data (``Cam`` folder), and the tensile data (``data_tensile`` folder), and the results (``results`` folder) with only the text version of the results, and
then use the ``tk_dic_viewer`` tool to generate all the relevant graphs and plots that the user requires.

