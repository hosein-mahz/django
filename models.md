
# Profile

* Profile
    * name
    * lastname
    * username
    * password
    * email
    * phone

# Caffee (Resturant)

* Caffee 
    * brand
    * name
    * address
    * user
    * avatar/logo/icon
    * location_x
    * location_y

* CaffeeFile
    * caffee_id
    * category (choise)
    * file

* Desk
    * caffee_id
    * category (choise)
    * desk_name

* Staff (v2)
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

* Order
    * profile_id
    * dateTime
    * price
    * delivery

* OrderSchedual
    * order_id
    * priority = 1
    * order_detail_id
    * dateTime

* OrderDetails
    * food_id
    * qty
