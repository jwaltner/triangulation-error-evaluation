
## Windows cmd
# docker build -t delme-pytorch-check -f pytorch-frc-dev.dockerfile .
# docker run -it --rm -p 8888:8888 -v %cd%:/workspace pytorch/pytorch:2.8.0-cuda12.9-cudnn9-runtime bash
## Windows powershell
# docker run -it --rm -p 8888:8888 -v ${PWD}:/workspace pytorch/pytorch:2.8.0-cuda12.9-cudnn9-runtime bash
FROM pytorch/pytorch:2.8.0-cuda12.9-cudnn9-runtime

# install git support into the development container so we can have git integration with VSCode.  without this,
# VSCode will not be able to perform git revisions when working in the development container.
# https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
# * always apt update prior to doing apt install to ensure latest available libraries.
# * -y selects "Yes" for all options.
# * DEBIAN_FRONTEND=noninteractive skips over user interactions for selecting timezone during the install
RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y git-all

# install jupyter notebook support and matplotlib for this development container
RUN pip install ipykernel matplotlib pandas

