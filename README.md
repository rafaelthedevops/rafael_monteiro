# rafael_monteiro
simple app deployed using ansible

1. Just clone the repo or unzip the file
2. (optional)if you have python installed on your host machine you can test with:

```
python simple_app.py
curl http://localhost:3000/something
```

3. I included a Vagrantfile so all you have to do is:

```
vagrant up
```

4. then run `vagrant ssh` to get into the provisioned machine and test it with curl 
```
curl http://localhost/hail
```
5. I chose to respond the http requests with json instead of plain text (I don't like plain text)
6. I configured the Vagrantfile to provide a box with the IP 192.168.200.10. so you can test with a browser if you want to
