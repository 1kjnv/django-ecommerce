<div align="center">
<h2 align="center">eBazar</h2>
<p align="center">e-commerce platform using Django and MySQL</p>
<table>
    <tr>
        <td>
            <img src="snapchots/shop.png" alt="shop" >
        </td>    
    </tr>
</table>

[![django](https://img.shields.io/badge/django%20versions-3.1.13-blue)](https://docs.djangoproject.com/en/3.0/)
[![mysql-client](https://img.shields.io/badge/mysql-client)](https://pypi.org/project/mysqlclient/)

</div>

<hr />
<div>
    <h4>Contents</h4>
    <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#requirements">Requirements to use</a></li>
        <li><a href="#contribution">Contribution</a></li>
    </ul>
</div>
<hr />


<div id="features">
    <h4>Features</h4>
    <p>eBazar - a shopping platform built with Django & MySQL with the following features:</p>
    <ul>
        <li>cart</li>
        <li>product search</li>
        <li>authentication</li>
        <li>product filtering</li>
        <li>payment(with Stripe)</li>
        <li>
            admin dashboard
            <ul>
                <li>product info</li>
                <li>product creation/deletion</li>
                <li>order details</li>
                <li>user info</li>
            </ul>
        </li>
    </ul>
    <p><strong>Note:</strong> you can also see snapchots of the above features in snapchots directory.</p>
</div>
<hr />

<div id="requirements">
<h4>Requirements to use!</h4>
<ol>
    <li>you need to have Python v3, Django v3 and MySQL installed on your machine</li>
    <li>create MySQL database and name it <strong>"ecommerce"</strong></li>
    <li>enter your database credentials(password, id, port, db name) in settings.py</li>
    <li>type: pip3 -r install requirements.txt (pip3 because this project runs on python3 and django version 3)</li>
    <li>open your CMD(Command Line) on Windows or Terminal on Mac</li>
    <li>go to the project directory</li>
    <li>type: source env/bin/activate - (to activate virtual env)</li>
    <li>type: cd ecommerce/</li>
    <li>type: python3 manage.py makemigrations</li>
    <li>type: python3 manage.py migrate</li>
    <li>type: python3 manage.py runserver</li>
</ol>
<p>And that's it!</p>
</div>

<hr />
<div id="contribution">
    <h4>Contributing</h4>
    <ul>
        <li>Provide the detailed explanation of your contribution</li>
        <li>Create Pull Request</li>
    </ul>
</div>