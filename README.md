<h1>eCommerce using Django(3.0) and MySQL</h1>
<hr>
<p>Simple yet Beautiful eCommerce application created with Django and MySQL.
    It has 2 user type:
    <ol>
        <li>Admin - can take control of all the stuff. For example
            <ul>
                <li>Create/Update/Delete products</li>
                <li>Can see user emails, names(not passwords!)</li>
            </ul>
        </li>
        <li>Customers - can the following:
            <ul>
                <li>Register</li>
                <li>Login/Logout</li>
                <li>Buy/Sell(Create products)</li>
                <li>Add to cart</li>
                <li>Remove from cart</li>
                <li>Edit profile</li>
            </ul>
        </li>
    </ol>
</p>
<p>To use this project you need to configure DB settings in ecommerce > ecommerce > settings.py</p>

<hr>
<h1>Snapchots from the project</h2>
<table>
    <tr>
        <td>
            <h4>Home</h4>
            <img src="snapchots/home.png" alt="home" width="500px" height="350px">
        </td>
        <td>
            <h4>Shop Page</h4>
            <img src="snapchots/shop.png" alt="shop" width="500px" height="350px">
        </td>    
    </tr>
    <tr>
        <td>
            <h4>Product Detail</h4>
            <img src="snapchots/product-detail.png" alt="product detail" width="500px" height="350px">
        </td>
        <td>
            <h4>Cart</h4>
            <img src="snapchots/cart.png" alt="cart" width="500px" height="350px">
        </td>
    </tr>
    <tr>
        <td>
            <h4>Login</h4>
            <img src="snapchots/login.png" alt="login" width="500px" height="350px">
        </td>
        <td>
            <h4>Sign up</h4>
            <img src="snapchots/reg.png" alt="register" width="500px" height="350px">
        </td>
    </tr>
    <tr>
        <td>
            <h4>Admin Dashboard</h4>
            <img src="snapchots/admin-dashboard.png" alt="admin dashboard" width="500px" height="350px">
        </td>
        <td>
            <h4>Admin Create Product</h4>
            <img src="snapchots/admin-product-create.png" alt="admin product create" width="500px" height="350px">
        </td>
    </tr>
    <tr>
        <td>
            <h4>Admin - Userlist</h4>
            <img src="snapchots/admin-userlist.png" alt="shop" width="500px" height="350px">
        </td>
    </tr>
</table>

<hr>
<h1>Requirements to use!</h1>
<p>To run this project on your local machine you need to do the following:
<ol>
    <li>you need to have python3 and django -version 3 installed on your machine</li>
    <li>you need to have MySQL installed on your machine</li>
    <li>need to have a MySQL database named 'ecommerce'</li>
    <li>enter your database password, id, port, db name in settings.py</li>
    <li>type: pip3 -r install requirements.txt (pip3 because this project runs on python3 and django version 3)</li>
    <li>go to commandline on windows or terminal on mac</li>
    <li>type: cd /django-ecommerce/</li>
    <li>type: source env/bin/activate - (to activate virtual env)</li>
    <li>type: cd ecommerce/</li>
    <li>type: python3 manage.py makemigrations</li>
    <li>type: python3 manage.py migrate</li>
    <li>type: python3 manage.py runserver</li>
</ol>
</p>

