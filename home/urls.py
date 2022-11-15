from django . urls import path,include
from. import views

urlpatterns =[
    path("",views.index,name="index"),
    path("checkout/",views.checkout,name="checkout"),
    path("cart/",views.cart,name="cart"),
    path("order/",views.order,name="order"),
    path("ordersingle/<int:pk>",views.ordersingle,name="ordersingle"),
    path("productsingle/<int:pk>",views.productsingle,name="productsingle"),
    path("success/",views.success,name="success"),
    path("product/",views.product,name="product"),

    path("cart/add/<int:pk>",views.cart_add,name="cartadd"),
    path("cart/remove/<int:pk>",views.cart_remove,name="cartremove"),
]