
# Profile

# Caffee (Resturant)

* Caffee 
    * brand
    * name
    * address
    * user
    * avatar/logo/icon

* CaffeeFile
    * caffee_id
    * category (choise)
    * file

* Desk
    * caffee_id
    * category (choise)
    * desk_name

* Staff
    * name
    * position
    * certification

# Food

* Food
    * id
    * caffee_id
    * title
    * attribute
    * image
    * gift
    * timeToDelivery

* Menu
    * id
    * title
    * caffee_id
    * food_id (oneToMany)
    * discount
    * price
    * start_date
    * end_date

# Delivery

* FoodOrder
    *