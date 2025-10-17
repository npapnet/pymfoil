PYMFOIL Workflow
================


Overview for scpirt
-------------------

This document describes the workflow for an pymfoil analysis (WORK IN PROGRESS.
the workfolow   is outlined in the following diagram. 

.. mermaid ::
    
   flowchart TD
        OutputFile["Output PDF File"]

        subgraph sUserDefined["User Preferences"]
            NACAType("NACA Type")
            Panels("No of Panels")
            OutputParams("Output Parameters and Format")
        end

        subgraph sPyfoil["pymfoil Package"]
            direction LR
            MFoil["Mfoil Object"]
            MFoilSolver["Mfoil Solver"]
            MFoil --> MFoilSolver
        end
        
        NACAType --> MFoil
        Panels --> MFoil
        OutputParams --> MFoilSolver
        MFoilSolver --> OutputFile


    classDef clInput fill:lightgreen,stroke:#333,stroke-width:4px;
    class NACAType,Panels,OutputParams clInput;

    classDef outputs fill:#f9f,stroke:#333,stroke-width:4px;
    class OutputFile outputs;

    classDef clSoftwareClass fill:lightblue,stroke:#333,stroke-width:4px;
    class Mfoil,MFoilSolver clSoftwareClass;

   
    %% classDef subgraph_padding fill:none,stroke-dasharray: 0 1
    %% class sRigidBodypadding,sRBKinematicspadding subgraph_padding 


Currently :

- the a simple analysis is shown in the ``examples\ex101-simple_usage.py\ex101.py`` file.


Overview for GUI
----------------
