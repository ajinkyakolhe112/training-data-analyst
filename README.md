## IMPORTANT LINKS
1. **CODE**. Custom Github Branch Link
    - www.tiny.cc/gcp-ajinkya
2. **LABS**. Qwiklabs LINK
    - https://googlecloud.qwiklabs.com
    - Exact URL- https://googlecloud.qwiklabs.com/classrooms/4706/labs/36518 
    - **Slides of Lectures will be present in googlecloud.qwiklabs.com**
    - If you don't see the training classroom, enter your email id at https://forms.gle/nwGkyr79SiZnMi587
3. **Github clone command**
    - Execute following command for official code repo
    - `git clone https://github.com/GoogleCloudPlatform/training-data-analyst`
    - Execute following command for custom code
    - `git clone --single-branch --branch gcp_custom https://github.com/ajinkyakolhe112/training-data-analyst.git`

### Misc
1. **DO NOT USE NANO**.
1. Launch UI text editor by executing command Use `cloudshell edit`

### Opening Juypter Notebook for Machine Learning
1. Login to Google Cloud Console
1. Go to Menu -> AI Platform -> Notebooks
2. Click on New Instance & Select Tensorflow 1.x, without GPU. (It takes around 1 minute to create the notebook & "Opening Jupyterlab becoming clickable.)
3. After Notebook Instance is created, click on Open Jupyterlab
4. Getting code in AI Platform Notebook
    1. After opening Jupyterlab, Select Terminal at bottom of the page
    1. Execute following command
        - `git clone --single-branch --branch gcp_custom https://github.com/ajinkyakolhe112/training-data-analyst.git`
        - **copy the above command & paste it in terminal of notebook by pressing shift + insert. Ctrl + v doesn't work.**
        - Once git clone is executed, code is copied into Jupyter Notebook
5. On left hand sidebar. There should be a folder training_data_analyst, click on it. It will show you the folder which contains the codes.
6. Open the corresponding notebook from the side bar, and execute the code by pressing `shift + enter`
