1. **myenv** file, put the MYREGION & ZONE. It should look like this.
   ```
    MYREGION=us-central1
    MYZONE=us-central1-c
    BUCKET=qwiklabs-gcp-b770345986805626
    BROWSER_IP=127.0.0.1
   ```
2. If you can't see output of echo $BUCKET, then execute `source myenv`
3. Instead of nano, use cloudshell edit command. the command would like like `cloudshell edit` and then create a new file called as myenv from the menu
4. If selected Component gateaway, choose image of Dataproc as 1.3 or 1.4
