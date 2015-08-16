
UWSGI configuration:
<pre>
<code>
<uwsgi>
    <socket>/tmp/flask.links.shop-the.com.sock</socket>
    <pythonpath>/home/shopper/sites/links.shop-the.com/api/</pythonpath>
    <module>app:app</module>
    <plugins>python27</plugins>
    <virtualenv>/home/shopper/env/</virtualenv>
    <disable-logging>true</disable-logging>
</uwsgi>
</code>
</pre>


Nginx configuration:

upstream flask_serv {
    server unix:/tmp/flask.links.shop-the.com.sock;
}

server {
    listen 80;
    server_name  links.shop-the.com;

    location  /  {
        uwsgi_pass  flask_serv;
        include  uwsgi_params;
    }

    access_log off;

    location  /static/ {
        root  /home/shopper/sites/links.shop-the.com/static;
    }
}
