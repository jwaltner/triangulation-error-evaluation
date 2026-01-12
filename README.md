## Background

This project includes example code and modules to assist with various calculations relevant to volunteer activites for the FIRST robotics competition Lake Monsters 2635 team and other STEM activities.

## AI Statement

Certain aspects of this project were written with the assistance of LLM's.  When a file leveraged LLM's in its creation, this fact will be annotated in the file header.  This code is provided for educational and research purposes and is not intended for commercial use.  While the code is being released with a permissive license which would allow commercial use, this permissive license only details the aspects of this code which have been authored "from scratch" or changed from the output of the LLM's in the event the code was derived from a LLM as a starting point.  It is left up to the end user of this code to determine if their use infringes on any other's work and determine if this library may be used directly in their own projects, whether they be educational or commercial.

It is not the intent of this project to copy any others' work, but to rather provide an examples of how certain calculations could be performed.  If it is found that this work copies others' work without attribution throught the use of the LLM's, please let me know and the project will either be updated with proper attribution or content will be removed.

## Project Usage

This project uses VSCode dev containers.  Prerequisites for using development containers is:
* docker (or podman) installed on the host machine.
* Dev Containers plugin installed in VSCode.

After opening the folder, you can use `CTRL+SHIFT+P` (or `CMD+SHIFT+P`) to `Dev Containers: Reopen Folder in Container` or similar.  There also may be a `Dev Containers: Rebuild` or `Dev Containers: Rebuild and Reopen...` option or similar.  After opening in Dev Containers, VS Code will perform a docker pull of the image referenced in the `.devcontainer/devcontainer.json` (the image reference may be contained in a referenced docker file).  After building the image, VSCode will reopen the folder and you will have the identical environment available to you as was used to build this project with no additional installations required.

If you want to exit the development container, select `Dev Containers: Reopen Folder Locally`.
