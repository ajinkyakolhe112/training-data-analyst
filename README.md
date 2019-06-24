## IMPORTANT LINKS
1. **CODE**. Custom Github Branch Link
    - www.tiny.cc/gcp-ajinkya
2. **LABS**. Qwiklabs LINK
    - https://www.googlecloud.qwiklabs.com
    - **Slides of Lectures will be present in googlecloud.qwiklabs.com**
3. **Github clone command**
    - Execute following command for official code repo
    - `git clone https://github.com/GoogleCloudPlatform/training-data-analyst`
    - Execute following command for custom code
    - `git clone --single-branch --branch gcp_training_custom https://github.com/ajinkyakolhe112/training-data-analyst.git`

### Misc
1. Use `cloudshell edit` command instead of `nano` command to open text editor

### Opening Juypter Notebook for Machine Learning
1. Go to Menu -> AI Platform -> Notebooks
2. Click on New Instance & Select Tensorflow 1.x, without GPU
3. After Notebook Instance is created, click on Open Jupyterlab
4. Getting code in AI Platform Notebook
    1. After opening Jupyterlab, Select Terminimal 
    1. Execute following command 
        - `git clone --single-branch --branch gcp_training_custom https://github.com/ajinkyakolhe112/training-data-analyst.git`
    1. **copy the above command & paste it in terminal of notebook by pressing shift + insert. Ctrl + v doesn't work. **
    1. Check on left hand sidebar. There should be a folder icon, click on it. It will show you the folder which contains the codes. 
    1. Open the corresponding notebook from the side bar, and execute the code by pressing `shift + enter` 
