

MAIN_ORDER_ID = 0
MAIN_ORDER_LIST = []

class Courier:
          

          def __init__(self, name, vehicle, speed, location:list):
                  
                  self.name = name
                  self.vehicle = vehicle
                  self.speed = speed
                  self.location = location 
                  self.isfree = True
          
          def move_to(self, destination:list):
                  
                  self.location = destination
          
          def deliver(self):
                  
                  print(f'We are delivering your order to {self.location}')
        

class Order:
        
        
        def __init__(self, order_id, address, status , customer):

                self.order_id = order_id
                self.address = address
                self.customer = customer

                allowed_status = ["awaiting", "delivering", "delivered"]

                if status in allowed_status: self.status = status
                else: print('You have entered wrong status, allowed statuses: "awaiting", "delivering", "delivered"')

        def update_status(self, status):
                    
                    allowed_status = ["awaiting", "delivering", "delivered"]
                        
                    if status in allowed_status: self.status = status
                    else: print('You have entered wrong status, allowed statuses: "awaiting", "delivering", "delivered"')
                        
                
class Customer:
        
        def __init__(self, name, address=None):
                
                self.name = name
                self.address = address
                self.orders_list = []
                self.orders_objects = []

        def make_order(self, order_address):
                            

               global MAIN_ORDER_ID
               MAIN_ORDER_ID+=1

               self.order_address = order_address
               self.order_id = MAIN_ORDER_ID
               MAIN_ORDER_LIST.append(self.order_id)
               self.orders_list.append(self.order_id)
               
               new_order = Order(self.order_id, self.order_address,'awaiting', self.name)
               self.orders_objects.append(new_order)

               return new_order


class DeliveryService:
        
        def __init__(self, couriers:list):
                
                self.courier_list=[]
                for courier in couriers:
                    self.courier_list.append(courier)
                


        def assign_order(self, order): 
            
               self.order = order

               for courier in self.courier_list: 
                   if courier.isfree:
                           courier.isfree = False
                           return courier

   


                    

        def simulate(self):
                
                # имитирует процесс доставки: курьер едет, статус меняется, заказ доставлен.

                print('Start')
                customer = Customer("Alice", [50,20])
                order = customer.make_order(customer.address)
                courier = ds.assign_order(customer.order_id)
                order.update_status('delivering')
                print('Have passed 3 days')
                courier.move_to(order.address)
                courier.deliver()
                order.update_status('delivered')
  



courier1 = Courier("Alice", "bike", 15, [0, 0])
courier2 = Courier("Bob", "car", 50, [10, 5])
courier3 = Courier("Charlie", "scooter", 25, [5, -3])
courier4 = Courier("Diana", "bike", 18, [2, 2])
courier5 = Courier("Ethan", "car", 55, [-4, 6])

courier_list = [courier1, courier2, courier3, courier4, courier5]

ds=DeliveryService(courier_list)

ds.simulate()
        
                 

